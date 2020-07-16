import React from 'react';
import { BrowserRouter as Router, Route, Redirect } from 'react-router-dom';
import Divider from "@material-ui/core/Divider";

import PrivateRoute from './PrivateRoute';
import SerialDecoder from './pages/SerialDecoder';
import ModelAdmin from './pages/ModelAdmin';
import Login from './pages/Login';
import NavBar from './components/NavBar';


function App(props) {

  return (
    <Router>
      <NavBar />
      <Divider />
      <div>
        <Route exact path="/" render={() => <Redirect to="/decoder" />} />
        <Route path="/login" render={(props) => <Login {...props} />} />
        <PrivateRoute path="/decoder" component={SerialDecoder} />
        <PrivateRoute path="/addmodels" component={ModelAdmin} />
      </div>
    </Router>
  );
}

export default App;
