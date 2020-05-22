import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { App } from './App';
import { rootReducer } from './store/rootReducer';
import * as serviceWorker from './serviceWorker';
import { StoreProvider } from './store/StoreProvider';
import { initialState } from './store/initialState';

ReactDOM.render(
  <React.StrictMode>
    <StoreProvider reducer={rootReducer} initialState={initialState}>
      <App />
    </StoreProvider>
  </React.StrictMode>,
  document.getElementById('root'),
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
