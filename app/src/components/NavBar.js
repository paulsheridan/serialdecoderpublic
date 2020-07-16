import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Cookies from "js-cookie";
import { useHistory } from "react-router-dom";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import IconButton from "@material-ui/core/IconButton";


const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

export default function SimpleNav() {
  const classes = useStyles();
  let history = useHistory();


  function logOut() {
    Cookies.remove('accessToken')
    history.push("/login");
  }

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <IconButton
            edge="start"
            className={classes.menuButton}
            color="inherit"
            aria-label="menu"
          ></IconButton>
          <Typography variant="h6" className={classes.title}>
            RPB Product Decoder
          </Typography>
          <Button variant="outlined" color="inherit" href="/decoder">
            Decode Serials
          </Button>
          <Button variant="outlined" color="inherit" href="/addmodels">
            Add Model Codes
          </Button>
          <Button variant="outlined" color="secondary" onClick={logOut}>
            Log out
          </Button>
        </Toolbar>
      </AppBar>
    </div>
  );
}
