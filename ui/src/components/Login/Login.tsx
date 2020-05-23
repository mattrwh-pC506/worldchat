import { get } from 'lodash';
import React, { useState, useEffect } from 'react';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import { createStyles, makeStyles, Theme } from '@material-ui/core/styles';
import { useStoreDispatch } from '../../store/useStoreHooks';
import { useUserSelectors } from '../../store/user/user.hooks';
import { loginUser } from '../../store/apis/auth.actions';

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      display: 'flex',
      flexDirection: 'column',
      width: '100vw',
      alignItems: 'center',
      transform: 'translateY(30vh)',
      '& > *': {
        width: '90vw',
        maxWidth: '400px',
      },
    },
    controls: {
      display: 'flex',
      marginTop: 15,
      width: 300,
      justifyContent: 'center',
    },
  }),
);

export const Login = () => {
  const dispatch = useStoreDispatch();
  const classes = useStyles();
  const [form, setForm] = useState({ username: '', password: '' });

  const handleChange = (fieldKey: string) => (event: any) => {
    const value = get(event, 'target.value', '');
    setForm((state: any) => ({ ...state, [fieldKey]: value }));
  };

  const submitForm = () => {
    const { username, password } = form;
    dispatch(loginUser({ username, password }));
  };

  const routeToRegister = () => {
    window.location.pathname = '/register';
  };

  const onSubmitMessageKeypress = (event: any) => {
    if (event.key == 'Enter') {
      submitForm();
    }
  };

  return (
    <section className={classes.root} onKeyPress={onSubmitMessageKeypress}>
      <TextField
        id="username"
        label="Username"
        type="username"
        variant="filled"
        value={form.username}
        onChange={handleChange('username')}
      />
      <TextField
        id="password"
        label="Password"
        type="password"
        variant="filled"
        value={form.password}
        onChange={handleChange('password')}
      />
      <section className={classes.controls}>
        <Button onClick={submitForm} variant="outlined">
          Submit Login
        </Button>
        <Button onClick={routeToRegister}>Register for An Account</Button>
      </section>
    </section>
  );
};
