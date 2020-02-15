import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import CabinetHeader from "./components/cabinetHeader/CabinetHeader";
import SignInPage from './pages/sign-in/SignIn';
import Logo from "./components/logo/Logo";
import CabinetSideBar from "./components/cabinetSideBar/CabinetSideBar";

function Routes() {
  return (
    <Router>
          <Switch>
            <Route path="/signIn">
                <Logo/>
                <SignInPage />
            </Route>
            <Route path="/account">
                <div id="content">
                    <CabinetHeader/>
                    <CabinetSideBar name="Yaroslav" lastName="Nestor"/>
                </div>
            </Route>
          </Switch>
        </Router>
         );
}

export default Routes;