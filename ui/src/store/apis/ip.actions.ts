import { get } from 'lodash';
import { AxiosResponse, AxiosError } from 'axios';
import { GenDispatch, IStoreRoot } from '../store.types';
import { api } from '../../api';
import { setIp } from '../user/user.actions';

export const lookupIp = (dispatch: GenDispatch, getState: () => IStoreRoot) => {
  api.get('https://api.ipify.org/?format=json').then((res: AxiosResponse) => {
    const ip = get(res.data, 'ip', '');
    dispatch(setIp({ ip }));
  });
};
