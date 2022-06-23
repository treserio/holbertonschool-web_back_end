#!/usr/bin/env python3
''' create an Authorization class for request verification '''
from api.v1.auth.auth import Auth
import typing as typ
import uuid
# from base64 import b64decode
# from models.user import User


class SessionAuth(Auth):
    ''' SessionAuth class for more advanced authentication '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        ''' that creates a Session ID for a user_id

            Args:
                user_id (str): the user_id for the current session

            Returns:

        '''
        if user_id and type(user_id) == str:
            sess_id = str(uuid.uuid4())
            self.user_id_by_session_id[sess_id] = user_id
            return sess_id

