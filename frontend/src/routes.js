import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import CabinetHeader from "./components/cabinetHeader/CabinetHeader";
import SignInPage from './pages/sign-in/SignIn';
import Logo from "./components/logo/Logo";
import CabinetSideBar from "./components/cabinetSideBar/CabinetSideBar";
import Header from "./components/header/Header";
import FilterSideBar from "./components/filterSideBar/FilterSideBar";

function Routes() {
  return (
    <Router>
          <Switch>
            <Route path="/signIn">
                <Logo/>
                <SignInPage />
            </Route>
            <Route path="/account/">
                <div id="content">
                    <CabinetHeader/>
                    <CabinetSideBar name="Yaroslav" lastName="Nestor"/>
                </div>
            </Route>
            <Route exact path="/data/films/">
                <Logo/>
                <Header/>
                <FilterSideBar/>
            </Route>
          </Switch>
        </Router>
         );
}

export default Routes;