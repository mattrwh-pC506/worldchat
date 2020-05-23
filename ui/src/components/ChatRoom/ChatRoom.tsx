import clsx from 'clsx';
import moment from 'moment';
import { get } from 'lodash';
import React, { useEffect, useState } from 'react';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import { createStyles, makeStyles, Theme } from '@material-ui/core/styles';

import { useStoreDispatch } from '../../store/useStoreHooks';
import { getOnlineChatters, getLoggedInChatter } from '../../store/apis/chatters.actions';
import { useChatSelectors } from '../../store/chat/chat.hooks';
import { NSChatStore } from '../../store/chat/chat.types';
import { ChatKeys } from '../../store/chat/chat.constants';
import { useUserSelectors } from '../../store/user/user.hooks';
import {
  sendMessage,
  connectToChat,
  joinChat,
  leaveChat,
} from '../../store/apis/messaging.actions';

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      display: 'flex',
      flexDirection: 'column',
      width: '100vw',
      alignItems: 'center',
      transform: 'translateY(8vh)',
      '& > *': {
        width: '90vw',
        maxWidth: '600px',
      },
    },
    messageInput: {
      display: 'flex',
    },
    chatInput: {
      width: 300,
    },
    chatBox: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'flex-start',
      minHeight: 300,
      margin: theme.spacing(1),
      borderRadius: 10,
      border: '1px solid #00f013',
      '& > *': {
        backgroundColor: '#4d4d4d',
        margin: theme.spacing(1),
        padding: theme.spacing(1),
        borderRadius: 10,
        opacity: 0.8,
        fontSize: 14,
      },
    },
    chatterList: {
      margin: theme.spacing(1),
      marginBottom: theme.spacing(2),
      display: 'flex',
      alignItems: 'flex-start',
      maxHeight: 400,
      flexWrap: 'wrap',
      overflowY: 'auto',
      '& > *': {
        border: '1px solid #00f013',
        backgroundColor: '#4d4d4d',
        padding: theme.spacing(1),
        borderRadius: 10,
        opacity: 0.8,
        marginRight: 5,
        marginTop: 5,
        fontSize: 8,
      },
    },
    button: {
      maxWidth: 200,
      border: '1px solid #08cb17',
      borderRadius: 10,
    },
    logout: {
      position: 'fixed',
      top: '5px',
      right: '5px',
    },
    leaveButtonContainer: {
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'flex-start',
    },
  }),
);

export const ChatRoom = () => {
  const dispatch = useStoreDispatch();
  const classes = useStyles();
  const { chatters, messages } = useChatSelectors(ChatKeys.RANDOM_CHAT);
  const { user } = useUserSelectors();
  const [joined, setJoined] = useState(false);
  const [message, setMessage] = useState('');

  const username = user.username;

  useEffect(() => {
    dispatch(getOnlineChatters);
    dispatch(connectToChat);
    dispatch(getLoggedInChatter);
  }, []);

  useEffect(() => {
    if (joined) {
      dispatch(getOnlineChatters);
    }
  }, [joined]);

  const chatter = () => {
    const matches = chatters.filter(
      (chatter: NSChatStore.IChatter) => chatter.username === user.username,
    );
    const match = matches[0] as NSChatStore.IChatter;
    return {
      username: get(match, 'username', user.username),
      usertag: get(match, 'usertag', user.usertag),
      address: get(match, 'address', user.address || ''),
      distance: get(match, 'distance', '0'),
    };
  };

  const handleJoin = () => {
    setJoined(true);
    joinChat(chatter());
  };

  const handleLeave = () => {
    setJoined(false);
    leaveChat(chatter());
  };

  const handleMessageChange = (event: any) => {
    const value = get(event, 'target.value', '');
    setMessage(value);
  };

  const submitMessage = () => {
    const messageObj = {
      text: message,
      chatter: chatter(),
      datetime: moment().format('LLLL'),
    };
    sendMessage(messageObj);
    setMessage('');
  };

  const onSubmitMessageKeypress = (event: any) => {
    if (event.key == 'Enter') {
      submitMessage();
    }
  };

  const handleLogout = () => {
    sessionStorage.removeItem('token');
    window.location.pathname = '/login';
  };

  const renderChatters = () => {
    return chatters.map((chatter: NSChatStore.IChatter) => {
      return (
        <div>
          <div>
            <strong>{chatter.username}</strong> - <em>{chatter.usertag}</em>
          </div>
          <div>{chatter.address}</div>
        </div>
      );
    });
  };

  const renderJoinButton = () => {
    return (
      <Button className={classes.button} onClick={handleJoin}>
        Join Global Chat!
      </Button>
    );
  };

  const renderLeaveButton = () => {
    return (
      <Button className={classes.button} onClick={handleLeave}>
        Leave Global Chat
      </Button>
    );
  };

  const renderPlaceholder = () => {
    return `(${user.username}): ...`;
  };

  const renderChatInput = () => {
    return (
      <section className={classes.messageInput}>
        <TextField
          className={classes.chatInput}
          variant="outlined"
          onChange={handleMessageChange}
          onKeyPress={onSubmitMessageKeypress}
          value={message}
          placeholder={renderPlaceholder()}
        />
        <Button onClick={submitMessage}>Send</Button>
      </section>
    );
  };

  const renderChatBox = () => {
    return messages.map((message: NSChatStore.IMessage) => {
      return (
        <span>
          <strong>{get(message, 'chatter.username', '')}</strong> said "{get(message, 'text', '')}"
          on <em>{get(message, 'datetime', '')}</em>
          <strong> From {get(message, 'chatter.distance', '')} miles away!</strong>
        </span>
      );
    });
  };

  const renderLogout = () => {
    return (
      <Button
        className={clsx(classes.button, classes.logout)}
        onClick={handleLogout}
        variant="outlined"
      >
        Logout
      </Button>
    );
  };

  const renderMainWindow = () => {
    if (joined && username) {
      return (
        <section className={classes.root}>
          <section>{renderChatInput()}</section>
          <section className={classes.chatBox}>{renderChatBox()}</section>
          <section className={classes.chatterList}>{renderChatters()}</section>
          <section className={classes.leaveButtonContainer}>{renderLeaveButton()}</section>
        </section>
      );
    } else if (username) {
      return <section className={classes.root}>{renderJoinButton()}</section>;
    } else {
      return null;
    }
  };

  return (
    <section>
      {renderLogout()}
      {renderMainWindow()}
    </section>
  );
};
