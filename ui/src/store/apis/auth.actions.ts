import { get } from 'lodash';
import { AxiosResponse, AxiosError } from 'axios';
import { GenDispatch, IStoreRoot } from '../store.types';
import { api, BASE_URL } from '../../api';
import { setUser } from '../user/user.actions';

export const isUsernameAvailable = (payload: { username: string }) => (
    dispatch: GenDispatch,
    getState: () => IStoreRoot,
) => {
    const { username } = payload;
    api.get(`${BASE_URL()}/authentication/usernameAvailable/${username}`).then(
        () => {},
        (error: AxiosError) => {
            alert(JSON.stringify(get(error, 'response.data.message', 'ui: unknown error'));
        },
            );
};

export const loginUser = (payload: { username: string; password: string }) => (
    dispatch: GenDispatch,
    getState: () => IStoreRoot,
) => {
    const { username, password } = payload;
    api
        .post(`${BASE_URL()}/authentication/login`, { username, password })
        .then(handleLoginSuccess(dispatch), handleLoginError);
};

export const registerUser = (payload: {
    username: string;
    password: string;
    usertag: string;
    address: string;
    geocode: string;
}) => (dispatch: GenDispatch, getState: () => IStoreRoot) => {
    const { username, password, usertag, address, geocode } = payload;
    const registrationApi = (geocode: string) => {
        api
            .post(`${BASE_URL()}/authentication/register`, {
                username,
                password,
                usertag,
                address,
                geocode,
            })
            .then(handleLoginSuccess(dispatch), handleLoginError);
    };

    api.get(`${BASE_URL()}/locations/lookup/latlng/${address}`).then(
        (res: AxiosResponse) => {
            const verifiedGeocode: string = get(res.data, 'data', geocode);
            registrationApi(verifiedGeocode);
        },
        () => registrationApi(geocode),
    );
};

const handleLoginSuccess = (dispatch: GenDispatch) => (res: AxiosResponse) => {
    const { chatter, token } = res.data;
    dispatch(setUser({ user: chatter }));
    sessionStorage.setItem('token', token);
    window.location.pathname = '/chatroom';
};

const handleLoginError = (res: AxiosError) => {
    alert('Bad Login!');
};
