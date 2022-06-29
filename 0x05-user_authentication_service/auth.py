#!/usr/bin/env python3
''' authentication module '''
import bcrypt as bc
from db import DB
from user import User
# from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm.exc import NoResultFound
import bcrypt as bc
import uuid


def _hash_password(password: str) -> bytes:
    ''' a salted hash of the input password, hashed with bcrypt.hashpw.

        Args:
            password (str): the string to hash

        Returns:
            bytes: the byte representation of the input string
    '''
    return bc.hashpw(password.encode(), bc.gensalt(9))


def _generate_uuid() -> str:
    ''' generate a uuid string '''
    return str(uuid.uuid4())


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
                email (str): email tied to a User
                password (str): password to confirm is the User's

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

    def create_session(self, email: str) -> str:
        '''  returns the user's session ID as a string

            Args:
                email (str): email tied to a User

            Returns:
                str: the session ID of the user
        '''
        try:
            user = self._db.find_user_by(email=email)
            user.session_id = _generate_uuid()
            return user.session_id
        except NoResultFound:
            pass

    def get_user_from_session_id(self, session_id: str) -> User:
        ''' find a user by session_id

            Args:
                session_id (str): session_id tied to a User

            Returns:
                User: the user if found, else None
        '''
        try:
            return self._db.find_user_by(session_id=session_id)
        except Exception:
            return None
