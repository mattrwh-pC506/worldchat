import { get } from 'lodash';
import { AxiosResponse, AxiosError } from 'axios';
import { GenDispatch, IStoreRoot } from '../store.types';
import { api, headers, BASE_URL } from '../../api';
import { setChatters } from '../chat/chat.actions';
import { NSChatStore } from '../chat/chat.types';
import { ChatKeys } from '../chat/chat.constants';
import { setUser } from '../user/user.actions';
import { calculateDistance } from './location.actions';

export const getOnlineChatters = (dispatch: GenDispatch, getState: () => IStoreRoot) => {
  api.get(`${BASE_URL()}/chat/chatUsers`, { headers: headers() }).then((res: AxiosResponse) => {
    const chatters = get(res.data, 'chatters', []);
    dispatch(setChatters(ChatKeys.RANDOM_CHAT)({ chatters }));
  });
};

export const getLoggedInChatter = (dispatch: GenDispatch, getState: () => IStoreRoot) => {
  api.get(`${BASE_URL()}/chat/chatUser`, { headers: headers() }).then((res: AxiosResponse) => {
    const chatter = get(res.data, 'chatter', {});
    dispatch(setUser({ user: chatter }));
  });
};
