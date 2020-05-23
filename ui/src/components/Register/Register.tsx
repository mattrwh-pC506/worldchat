import { get } from 'lodash';
import React, { useState, useEffect } from 'react';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import { createStyles, makeStyles, Theme } from '@material-ui/core/styles';
import { useStoreDispatch } from '../../store/useStoreHooks';
import { useUserSelectors } from '../../store/user/user.hooks';
import { registerUser, isUsernameAvailable } from '../../store/apis/auth.actions';

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
  }),
);

export const Register = () => {
  const dispatch = useStoreDispatch();
  const { address: addressFromState, geocode } = useUserSelectors();
  const classes = useStyles();
  const [form, setForm] = useState({
    username: '',
    password: '',
    usertag: '',
    address: '',
  });

  useEffect(() => {
    setForm((state: any) => ({ ...state, address: addressFromState }));
  }, [addressFromState]);

  const handleChange = (fieldKey: string) => (event: any) => {
    const value = get(event, 'target.value', '');
    setForm((state: any) => ({ ...state, [fieldKey]: value }));
  };

  const submitForm = () => {
    const { username, password, usertag, address } = form;
    dispatch(registerUser({ username, password, usertag, geocode, address }));
  };

  const routeToLogin = () => {
    window.location.pathname = '/login';
  };

  const checkAvailability = () => {
    const { username } = form;
    dispatch(isUsernameAvailable({ username }));
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
        type="username"
        label="Username"
        variant="filled"
        value={form.username}
        onChange={handleChange('username')}
        onBlur={checkAvailability}
      />
      <TextField
        id="password"
        type="password"
        label="Password"
        variant="filled"
        value={form.password}
        onChange={handleChange('password')}
      />
      <TextField
        id="usertag"
        label="Usertag"
        variant="filled"
        value={form.usertag}
        onChange={handleChange('usertag')}
      />
      <TextField
        id="address"
        label="Address"
        variant="filled"
        value={form.address}
        onChange={handleChange('address')}
      />
      <Button onClick={submitForm}>Register</Button>
      <Button onClick={routeToLogin}>Login Instead</Button>
    </section>
  );
};
