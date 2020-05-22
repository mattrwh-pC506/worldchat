import { ActionTypes } from '../action.types';
import { NSUserStore } from './user.types';

export const setUser = (payload: { user: NSUserStore.IRoot }) => {
  return { type: ActionTypes.SET_USER, payload };
};

export const setIp = (payload: { ip: string }) => {
  return { type: ActionTypes.SET_IP, payload };
};

export const setAddress = (payload: { address: string }) => {
  return { type: ActionTypes.SET_ADDRESS, payload };
};

export const setGeocode = (payload: { geocode: string }) => {
  return { type: ActionTypes.SET_GEOCODE, payload };
};
