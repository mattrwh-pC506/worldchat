import { flow } from 'lodash';
import { IStoreRoot } from '../store.types';
import { NSUserStore } from './user.types';

export const userSelector = (state: IStoreRoot): NSUserStore.IRoot => state.user;
export const ipSelector = flow(
  userSelector,
  (user: NSUserStore.IRoot) => user.ip || '',
);
export const geocodeSelector = flow(
  userSelector,
  (user: NSUserStore.IRoot) => user.geocode || '',
);
export const addressSelector = flow(
  userSelector,
  (user: NSUserStore.IRoot) => user.address || '',
);
