import { initialState } from './initialState';
import { Action, AsyncAction, IStoreRoot } from './store.types';
import { chatReducer } from './chat/chat.reducer';
import { userReducer } from './user/user.reducer';

(window as any).store = initialState;

export const rootReducer = (state: IStoreRoot = initialState, _action: Action | AsyncAction) => {
  const action = _action as Required<Action>;
  const store = {
    chat: chatReducer(state.chat, action),
    user: userReducer(state.user, action),
  };
  (window as any).store = store;
  return store;
};
