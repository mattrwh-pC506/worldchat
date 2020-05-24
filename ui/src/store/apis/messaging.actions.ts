import axios, { AxiosResponse, AxiosError } from 'axios';
import { get, includes } from 'lodash';
import { GenDispatch, IStoreRoot } from '../store.types';
import { ActionTypes } from '../action.types';
import { NSChatStore } from '../chat/chat.types';
import { ChatKeys } from '../chat/chat.constants';
import { chatterJoined, chatterLeft, newMessage } from '../chat/chat.actions';
import { calculateDistance } from './location.actions';
import { getOnlineChatters } from './chatters.actions';
import { BASE_WSS_URL } from '../../api';

let ws: WebSocket = new WebSocket(`${BASE_WSS_URL()}/ws/chat/global/`);

export const connectToChat = (dispatch: GenDispatch, getState: () => IStoreRoot) => {
  dispatch(chatListeners());
};

export const sendMessage = (message: NSChatStore.IMessage) => {
  ws.send(JSON.stringify({ type: ActionTypes.NEW_MESSAGE, message }));
};

export const joinChat = (chatter: NSChatStore.IChatter) => {
  ws.send(JSON.stringify({ type: ActionTypes.CHATTER_JOINED, chatter }));
};

export const leaveChat = (chatter: NSChatStore.IChatter) => {
  ws.send(JSON.stringify({ type: ActionTypes.CHATTER_LEFT, chatter }));
};

const messageHandler = (dispatch: GenDispatch) => (event: { data: string }) => {
  const chatKey = ChatKeys.RANDOM_CHAT;
  const messagePayload: any = JSON.parse(event.data);
  const { type, chatter = {}, chatters = [], message = {} } = messagePayload;
  switch (type) {
    case ActionTypes.CHATTER_JOINED:
      setTimeout(() => {
        dispatch(getOnlineChatters);
      }, 500);
      break;
    case ActionTypes.CHATTER_LEFT:
      setTimeout(() => {
        dispatch(getOnlineChatters);
      }, 500);
      break;
    case ActionTypes.NEW_MESSAGE:
      dispatch(newMessage(chatKey)({ message }));
      break;
  }
};

const chatListeners = () => (dispatch: GenDispatch, getState: () => IStoreRoot) => {
  ws.addEventListener('message', messageHandler(dispatch));
};
