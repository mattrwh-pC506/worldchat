import axios from 'axios';
import { filter, keys, isNil, negate } from 'lodash';

export const api = axios.create({
  maxRedirects: 10,
  baseURL: '',
});

export const BASE_URL = () => {
  const host = window.location.hostname;
  if (host === 'localhost' || host === '0.0.0.0' || host === '127.0.0.1') {
    return 'http://localhost:8000';
  } else {
    return 'https://vast-earth-99742.herokuapp.com';
  }
};

export const BASE_WSS_URL = () => {
  const host = window.location.hostname;
  if (host === 'localhost' || host === '0.0.0.0' || host === '127.0.0.1') {
    return 'ws://localhost:8000';
  } else {
    return 'wss://vast-earth-99742.herokuapp.com';
  }
};

export const headers = () => {
  const token = sessionStorage.getItem('token');
  return { Authorization: `Bearer ${token}` };
};

export const buildParams = (params: { [key: string]: any }): URLSearchParams => {
  const isNotNil = negate(isNil);
  const filledParams = filter(keys(params), (key: string) => isNotNil(params[key]));
  const urlSearchParams = new URLSearchParams();
  filledParams.forEach((filledParam: string) => {
    urlSearchParams.append(filledParam, params[filledParam]);
  });
  return urlSearchParams;
};
