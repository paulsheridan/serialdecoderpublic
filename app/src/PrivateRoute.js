import React from "react";
import { Route, Redirect } from "react-router-dom";
import Cookies from "js-cookie";


function PrivateRoute({ component: Component, ...rest }) {

  return (
    <Route
      {...rest}
      render={props =>
        Cookies.get('accessToken') ? (
          <Component {...props} />
        ) : (
          <Redirect
            to={{ pathname: "/login", state: { referer: props.location } }}
          />
        )
      }
    />
  );
}

export default PrivateRoute;
