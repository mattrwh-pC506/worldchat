import { IStoreRoot } from './store.types';
import { initialChatState } from './chat/chat.reducer';
import { initialUserState } from './user/user.reducer';

export const initialState: IStoreRoot = {
  chat: initialChatState,
  user: initialUserState,
};
