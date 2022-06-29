#!/usr/bin/env python3
''' authentication module '''
import bcrypt as bc
from db import DB
from user import User
# from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm.exc import NoResultFound
import bcrypt as bc


def _hash_password(password: str) -> bytes:
    ''' a salted hash of the input password, hashed with bcrypt.hashpw.

        Args:
            password (str): the string to hash

        Returns:
            bytes: the byte representation of the input string
    '''
    return bc.hashpw(password.encode(), bc.gensalt(9))


class Auth:
    ''' auth class to interact with the authentication database.
    '''

    def __init__(self):
        ''' initialize instance of Auth '''
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        ''' create and save a new user instance if it doesn't exist in the db

            Args:
                email (str): email to use for new User
                password (str): password to use for new User

            Returns:
                User: the new User stored(registered) in the db
        '''
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        ''' locate the user by email. Check the password with bcrypt.checkpw.
        If it matches return True. In any other case, return False.

            Args:
                email (str): email to use for new User
                password (str): password to use for new User

            Returns:
                bool: True if password matches, else False
        '''
        try:
            return bc.checkpw(
                password.encode('utf-8'),
                self._db.find_user_by(email=email).hashed_password
            )
        except Exception:
            return False
