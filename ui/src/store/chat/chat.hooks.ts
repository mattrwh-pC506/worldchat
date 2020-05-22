import { useStoreDispatch, useStoreSelector } from '../useStoreHooks';
import { ChatKeys } from './chat.constants';
import { NSChatStore } from './chat.types';
import { setChatSession, newMessage } from './chat.actions';

import { chatKeySelector, chattersSelector, messagesSelector } from './chat.selectors';

export const useChatActionCreators = (key: ChatKeys) => {
  const dispatch = useStoreDispatch();
  return {
    setChatSession: (payload: { roomName: string; chatters: NSChatStore.IChatter[] }) =>
      dispatch(setChatSession(key)(payload)),
    newMessage: (payload: { message: NSChatStore.IMessage }) => dispatch(newMessage(key)(payload)),
  };
};

export const useChatSelectors = (key: ChatKeys) => {
  const chat = useStoreSelector(chatKeySelector(key)) as NSChatStore.IChat;
  const chatters = useStoreSelector(chattersSelector(key)) as NSChatStore.IChatter[];
  const messages = useStoreSelector(messagesSelector(key)) as NSChatStore.IMessage[];
  return { chat, chatters, messages };
};
