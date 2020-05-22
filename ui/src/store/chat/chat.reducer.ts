import { uniqBy, constant, keys, times, zipObject } from 'lodash';
import { ActionTypes } from '../action.types';
import { GenAction } from '../store.types';
import { NSChatStore } from './chat.types';
import { ChatKeys } from './chat.constants';

export const initialChatState: NSChatStore.IRoot = zipObject(
  keys(ChatKeys),
  times(
    keys(ChatKeys).length,
    constant({
      roomName: '',
      chatters: [],
      messages: [],
    }),
  ),
);

const handleSetChatSession = (state: NSChatStore.IChat, action: GenAction) => {
  return {
    ...state,
    ...action.payload,
  };
};

const handleNewMessage = (state: NSChatStore.IChat, action: GenAction) => {
  const { message } = action.payload;
  const matches = state.chatters.filter(
    (chatter: NSChatStore.IChatter) => chatter.username === message.chatter.username,
  );
  const match = matches[0] as NSChatStore.IChatter;
  message.chatter.distance = match.distance;

  return {
    ...state,
    messages: [...state.messages, message],
  };
};

const handleChatterJoined = (state: NSChatStore.IChat, action: GenAction) => {
  const { chatter } = action.payload;
  const chatters = [
    ...state.chatters.filter(
      (existingChatter: NSChatStore.IChatter) => existingChatter.username !== chatter.username,
    ),
    chatter,
  ];
  return { ...state, chatters };
};

const handleChatterLeft = (state: NSChatStore.IChat, action: GenAction) => {
  const { chatter } = action.payload;
  const chatters = state.chatters.filter(
    (existingChatter: NSChatStore.IChatter) => existingChatter.username !== chatter.username,
  );
  return { ...state, chatters };
};

const handleSetChatters = (state: NSChatStore.IChat, action: GenAction) => {
  const { chatters } = action.payload;
  const newChatters = [...state.chatters, ...chatters];
  return {
    ...state,
    chatters: uniqBy(newChatters, (chatter: NSChatStore.IChatter) => chatter.username),
  };
};

const handleSetChatterDistance = (state: NSChatStore.IChat, action: GenAction) => {
  const { chatter, distance } = action.payload;
  const chatters = state.chatters.map((chatter: NSChatStore.IChatter) => {
    if (chatter.username === chatter.username) {
      chatter.distance = distance;
    }
    return chatter;
  });
  return { ...state, chatters };
};

export const chatReducer = (state = initialChatState, action: GenAction) => {
  const { key } = action;
  switch (action.type) {
    case ActionTypes.SET_CHAT_SESSION:
      return { ...state, [key]: handleSetChatSession(state[key], action) };
    case ActionTypes.NEW_MESSAGE:
      return { ...state, [key]: handleNewMessage(state[key], action) };
    case ActionTypes.CHATTER_JOINED:
      return { ...state, [key]: handleChatterJoined(state[key], action) };
    case ActionTypes.CHATTER_LEFT:
      return { ...state, [key]: handleChatterLeft(state[key], action) };
    case ActionTypes.SET_CHATTERS:
      return { ...state, [key]: handleSetChatters(state[key], action) };
    case ActionTypes.SET_CHATTER_DISTANCE:
      console.log('DISTANCE ');
      return { ...state, [key]: handleSetChatterDistance(state[key], action) };
    default:
      return state;
  }
};
