#!/usr/bin/env python3
""" Check responses to app.py endpoints
"""
import requests


def register_user(email: str, password: str) -> None:
    ''' testing POST to http://0.0.0.0:5000/users with email & password

        Args:
            email (str): email to test
            password (str): password to test
    '''
    res = requests.post(
        'http://0.0.0.0:5000/users',
        data={'email': email, 'password': password}
    )
    assert res.status_code == 200
    assert res.headers.get('content-type') == 'application/json'
    assert res.json() == {'email': email, 'message': 'user created'}


def log_in_wrong_password(email: str, password: str) -> None:
    ''' test logging user in with wrong password

        Args:
            email (str): the email tied to the user account
            password (str): the user's incorrect password
    '''
    res = requests.post(
        'http://0.0.0.0:5000/sessions',
        data={'email': email, 'password': password}
    )
    assert res.status_code == 401
    assert res.reason == 'UNAUTHORIZED'


def log_in(email: str, password: str) -> str:
    ''' test logging user in with correct password

        Args:
            email (str): the email tied to the user account
            password (str): the user's incorrect password
    '''
    res = requests.post(
        'http://0.0.0.0:5000/sessions',
        data={'email': email, 'password': password}
    )
    assert res.status_code == 200
    assert res.cookies['session_id'] is not None
    assert res.headers.get('content-type') == 'application/json'
    assert res.json() == {'email': EMAIL, 'message': 'logged in'}
    return res.cookies['session_id']


def profile_unlogged() -> None:
    ''' check for a user that isn't in an active session '''
    res = requests.get(
        'http://0.0.0.0:5000/profile'
    )
    assert res.status_code == 403
    assert res.reason == 'FORBIDDEN'


def profile_logged(session_id: str) -> None:
    ''' test finding a user profile that has an active session

        Args:
            session_id (str): an active session id for a user
    '''
    res = requests.post(
        'http://0.0.0.0:5000/profile',
        cookies={'session_id': session_id}
    )
    assert res.status_code == 200
    assert res.headers.get('content-type') == 'application/json'
    assert res.json() == {'email': EMAIL}
    assert res.cookies['session_id'] == session_id


def log_out(session_id: str) -> None:
    ''' test removing the session id for an active user

        Args:
            session_id (str): an active session id for a user
    '''
    res = requests.delete(
        'http://0.0.0.0:5000/sessions',
        cookies={'session_id': session_id}
    )
    assert res.status_code == 200
    assert res.url == 'http://0.0.0.0:5000/'
    assert res.headers.get('content-type') == 'application/json'
    assert res.json() == {'message': 'Bienvenue'}


def reset_password_token(email: str) -> str:
    ''' test the reset_token endpoint

        Args:
            email (str): the email tied to the user account

        Returns:
            str: the reset token for the user
    '''
    res = requests.post(
        'http://0.0.0.0:5000/reset_password',
        data={'email': email}
    )
    assert res.status_code == 200
    assert res.headers.get('content-type') == 'application/json'
    assert {'email', 'reset_token'}.issubset(set(res.json().keys()))
    return res.json()['reset_token']


def update_password(email: str, reset_token: str, new_password: str) -> None:
    ''' test the update_password functionality of reset_password

        Args:
            email (str): the email tied to the user account
            reset_token (str): the user's previously provided reset token
            new_password (str): the user's new password to use
    '''
    res = requests.put(
        'http://0.0.0.0:5000/reset_password',
        data={
            'email': email,
            'reset_token': reset_token,
            'new_password': new_password
        }
    )
    assert res.status_code == 200
    assert res.headers.get('content-type') == 'application/json'
    assert res.json() == {'email': email, 'message': 'Password updated'}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
