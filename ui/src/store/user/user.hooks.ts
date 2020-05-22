import { useStoreDispatch, useStoreSelector } from '../useStoreHooks';
import { NSUserStore } from './user.types';
import { setUser, setIp } from './user.actions';
import { userSelector, ipSelector, geocodeSelector, addressSelector } from './user.selectors';

export const useUserActionCreators = () => {
  const dispatch = useStoreDispatch();
  return {
    setUser: (payload: { user: NSUserStore.IRoot }) => dispatch(setUser(payload)),
    setIp: (payload: { ip: string }) => dispatch(setIp(payload)),
  };
};

export const useUserSelectors = () => {
  const user = useStoreSelector(userSelector);
  const ip = useStoreSelector(ipSelector);
  const geocode = useStoreSelector(geocodeSelector);
  const address = useStoreSelector(addressSelector);
  return { user, ip, geocode, address };
};
