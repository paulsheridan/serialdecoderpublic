import React, { useState } from 'react';
import { Redirect } from 'react-router-dom';
import axios from 'axios';
import { GoogleLogin } from 'react-google-login';
import Cookies from "js-cookie";


function Login(props) {

  const [isLoggedIn, setLoggedIn] = useState(false);
  const [isError, setIsError] = useState(false);
  let referer = "";

  try {
    referer = props.location.state.referer || "/";
  }
  catch (error) {
    if (error instanceof TypeError) {
      referer = "/";
    }
  }

  function postLogin(userInfo) {
    axios
      .post("http://localhost:5000/graphql", {
        query: `
      mutation {
        tokenAuth(idToken: ${JSON.stringify(userInfo.tokenId)}) {
          token {
            accessToken
          }
        }
      }
      `,
      })
      .then((response) => {
        Cookies.set(
          "accessToken",
          response.data.data.tokenAuth.token.accessToken,
          { expires: 1 }
        );
        setLoggedIn(true);
      })
      .catch((e) => {
        setIsError(true);
      });
  }

  if (isLoggedIn) {
    return <Redirect to={referer} />;
  }

  return (
      <div>
        <GoogleLogin
          clientId="161417844290-ueic5i3perjmooskhmoea4mk9a542mm1.apps.googleusercontent.com"
          buttonText="Sign in with Google"
          onSuccess={postLogin}
        />
      </div>
  );
}

export default Login;
