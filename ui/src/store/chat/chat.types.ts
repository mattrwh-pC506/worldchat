import { ChatKeys } from './chat.constants';

export declare namespace NSChatStore {
  export interface IRoot {
    [k: string]: IChat;
  }

  export interface IChat {
    roomName: string;
    chatters: IChatter[];
    messages: IMessage[];
  }

  export interface IChatter {
    username: string;
    usertag: string;
    address: string;
    distance?: string;
  }

  export interface IMessage {
    text: string;
    datetime: string;
    chatter: IChatter;
  }
}
