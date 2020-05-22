import { Dispatch } from 'react';
import { ActionTypes } from './action.types';
import { NSChatStore } from './chat/chat.types';
import { NSUserStore } from './user/user.types';

export interface IStoreRoot {
  chat: NSChatStore.IRoot;
  user: NSUserStore.IRoot;
}

export type ActionPayload = any;

export interface Action {
  type: ActionTypes;
  key?: string;
  payload?: ActionPayload;
}

export type ActionWithPayload = Required<Action>;
export type AsyncAction = Dispatch<Action>;
export type AsyncActionWithPayload = Dispatch<ActionWithPayload>;

export type GenAction = Action | AsyncAction | ActionWithPayload | AsyncActionWithPayload | any;
export type GenDispatch = Dispatch<GenAction>;
