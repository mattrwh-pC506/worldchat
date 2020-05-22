import { includes, filter, flow, get } from 'lodash';
import { IStoreRoot } from '../store.types';
import { NSChatStore } from './chat.types';
import { ChatKeys } from './chat.constants';

const chatRootSelector = (state: IStoreRoot) => state.chat;

export const chatKeySelector = (key: ChatKeys) =>
  flow(
    chatRootSelector,
    (root: NSChatStore.IRoot) => get(root, [key], {}),
  );

export const chattersSelector = (key: ChatKeys) =>
  flow(
    chatKeySelector(key),
    (chat: NSChatStore.IChat) => get(chat, 'chatters', []) as NSChatStore.IChatter[],
  );

export const messagesSelector = (key: ChatKeys) =>
  flow(
    chatKeySelector(key),
    (chat: NSChatStore.IChat) => get(chat, 'messages', []),
  );
