import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import './App.css';

import { useStoreDispatch } from './store/useStoreHooks';
import { ChatRoom } from './components/ChatRoom/ChatRoom';
import { Login } from './components/Login/Login';
import { Register } from './components/Register/Register';
import { ping } from './store/apis/ping.actions';
import { lookupGeocodeByIp, lookupAddressByGeocode } from './store/apis/location.actions';
import { lookupIp } from './store/apis/ip.actions';
import { useUserSelectors } from './store/user/user.hooks';

export const App = () => {
  const dispatch = useStoreDispatch();
  const { ip, geocode, address } = useUserSelectors();
  const onLoginPage = window.location.pathname === '/login';
  const onRegisterPage = window.location.pathname === '/register';
  const onAuthPage = onLoginPage || onRegisterPage;

  useEffect(() => {
    if (onAuthPage) {
      dispatch(lookupIp);
    }
    const token = sessionStorage.getItem('token');
    if (!token && !onLoginPage && !onRegisterPage) {
      window.location.pathname = '/login';
    } else if (token && (onLoginPage || onRegisterPage)) {
      window.location.pathname = '/chatroom';
    }
  }, []);

  useEffect(() => {
    if (!!ip && onAuthPage) {
      dispatch(lookupGeocodeByIp(ip));
    }
  }, [ip]);

  useEffect(() => {
    if (!!geocode && onAuthPage) {
      dispatch(lookupAddressByGeocode(geocode));
    }
  }, [geocode]);

  useEffect(() => {
    const pingInterval = setInterval(() => {
      if (!onLoginPage && !onRegisterPage) {
        dispatch(ping);
      }
    }, 30000);
    return () => clearInterval(pingInterval);
  }, [address]);

  return (
    <div className="App">
      <Router>
        <Switch>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/register">
            <Register />
          </Route>
          <Route path="/chatroom">
            <ChatRoom />
          </Route>
        </Switch>
      </Router>
    </div>
  );
};
