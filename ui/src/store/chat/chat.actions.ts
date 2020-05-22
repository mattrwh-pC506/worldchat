import { ActionTypes } from '../action.types';
import { NSChatStore } from './chat.types';
import { ChatKeys } from './chat.constants';

export const setChatSession = (key: ChatKeys) => (payload: {
  roomName: string;
  chatters: NSChatStore.IChatter[];
}) => {
  return { key, type: ActionTypes.SET_CHAT_SESSION, payload };
};

export const chatterJoined = (key: ChatKeys) => (payload: { chatter: NSChatStore.IChatter }) => {
  return { key, type: ActionTypes.CHATTER_JOINED, payload };
};

export const chatterLeft = (key: ChatKeys) => (payload: { chatter: NSChatStore.IChatter }) => {
  return { key, type: ActionTypes.CHATTER_LEFT, payload };
};

export const newMessage = (key: ChatKeys) => (payload: { message: NSChatStore.IMessage }) => {
  return { key, type: ActionTypes.NEW_MESSAGE, payload };
};

export const setChatters = (key: ChatKeys) => (payload: { chatters: NSChatStore.IChatter[] }) => {
  return { key, type: ActionTypes.SET_CHATTERS, payload };
};

export const setChatterDistance = (key: ChatKeys) => (payload: {
  chatter: NSChatStore.IChatter;
  distance: string;
}) => {
  return { key, type: ActionTypes.SET_CHATTER_DISTANCE, payload };
};
