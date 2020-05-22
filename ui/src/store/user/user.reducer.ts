import { ActionTypes } from '../action.types';
import { GenAction } from '../store.types';
import { NSUserStore } from './user.types';

export const initialUserState: NSUserStore.IRoot = {
  username: '',
  usertag: '',
  geocode: '',
  address: '',
  ip: '',
};

const handleSetUser = (state: NSUserStore.IRoot, action: GenAction) => {
  const { user } = action.payload;
  return { ...state, ...user };
};

const handleSetIp = (state: NSUserStore.IRoot, action: GenAction) => {
  const { ip } = action.payload;
  return { ...state, ip };
};

const handleSetAddress = (state: NSUserStore.IRoot, action: GenAction) => {
  const { address } = action.payload;
  return { ...state, address };
};

const handleSetGeocode = (state: NSUserStore.IRoot, action: GenAction) => {
  const { geocode } = action.payload;
  return { ...state, geocode };
};

export const userReducer = (state = initialUserState, action: GenAction) => {
  switch (action.type) {
    case ActionTypes.SET_USER:
      return handleSetUser(state, action);
    case ActionTypes.SET_IP:
      return handleSetIp(state, action);
    case ActionTypes.SET_ADDRESS:
      return handleSetAddress(state, action);
    case ActionTypes.SET_GEOCODE:
      return handleSetGeocode(state, action);
    default:
      return state;
  }
};
