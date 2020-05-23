import { get } from 'lodash';
import { AxiosResponse, AxiosError } from 'axios';
import { GenDispatch, IStoreRoot } from '../store.types';
import { api, headers, BASE_URL } from '../../api';

export const ping = (dispatch: GenDispatch, getState: () => IStoreRoot) => {
  api.get(`${BASE_URL()}/authentication/ping`, { headers: headers() }).then(
    (res: AxiosResponse) => {},
    (res: AxiosError) => {
      window.location.pathname = '/login';
    },
  );
};
