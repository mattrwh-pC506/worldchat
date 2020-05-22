import { GenDispatch, IStoreRoot } from './store.types';
import { useContext } from 'react';
import { StoreContext } from './StoreContext';

const useStoreReducer = () => {
  const [, dispatch]: [IStoreRoot, GenDispatch] = useContext(StoreContext);
  const getState = () => (window as any).store;
  const enhancedDispatch = (action: any) => {
    if (!action.type) {
      action(enhancedDispatch, getState);
    } else {
      dispatch(action);
    }
  };
  return [getState(), enhancedDispatch] as [IStoreRoot, GenDispatch];
};

export const useStoreDispatch = () => {
  const [, dispatch] = useStoreReducer();
  return dispatch;
};

export const useStoreSelector = <T = {}>(selector: (state: IStoreRoot) => T) => {
  const [state] = useStoreReducer();
  return selector(state);
};
