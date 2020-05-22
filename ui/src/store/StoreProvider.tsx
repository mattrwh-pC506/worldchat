import React, { useReducer } from 'react';
import { StoreContext } from './StoreContext';

export const StoreProvider = ({ reducer, initialState, children }: any) => (
  <StoreContext.Provider value={useReducer(reducer, initialState)}>
    {children}
  </StoreContext.Provider>
);
