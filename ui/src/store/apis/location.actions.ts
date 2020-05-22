import { get } from 'lodash';
import { AxiosResponse, AxiosError } from 'axios';
import { GenDispatch, IStoreRoot } from '../store.types';
import { api, headers, BASE_URL } from '../../api';
import { setGeocode, setAddress } from '../user/user.actions';
import { NSChatStore } from '../chat/chat.types';
import { setChatterDistance } from '../chat/chat.actions';
import { ChatKeys } from '../chat/chat.constants';

export const lookupGeocodeByIp = (ip: string) => (
  dispatch: GenDispatch,
  getState: () => IStoreRoot,
) => {
  api.get(`${BASE_URL()}/locations/lookup/ip/${ip}`).then((res: AxiosResponse) => {
    const latitude = get(res.data, 'data.geolocation.latitude');
    const longitude = get(res.data, 'data.geolocation.longitude');
    const geocode = `${latitude},${longitude}`;
    dispatch(setGeocode({ geocode }));
  });
};

export const lookupAddressByGeocode = (geocode: string) => (
  dispatch: GenDispatch,
  getState: () => IStoreRoot,
) => {
  api.get(`${BASE_URL()}/locations/lookup/address/${geocode}`).then((res: AxiosResponse) => {
    const address = get(res.data, 'data');
    dispatch(setAddress({ address }));
  });
};

export const lookupLatLngByAddress = (address: string) => (
  dispatch: GenDispatch,
  getState: () => IStoreRoot,
) => {
  api.get(`${BASE_URL()}/locations/lookup/latlng/${address}`).then((res: AxiosResponse) => {
    const geocode = get(res.data, 'data');
    dispatch(setGeocode({ geocode }));
  });
};

export const calculateDistance = (otherChatter: NSChatStore.IChatter) => (
  dispatch: GenDispatch,
  getState: () => IStoreRoot,
) => {
  const otherUsername = otherChatter.username;
  api
    .get(`${BASE_URL()}/locations/lookup/distanceFromFriend/${otherUsername}`, {
      headers: headers(),
    })
    .then((res: AxiosResponse) => {
      const distance = get(res.data, 'data');
      dispatch(setChatterDistance(ChatKeys.RANDOM_CHAT)({ chatter: otherChatter, distance }));
    });
};
