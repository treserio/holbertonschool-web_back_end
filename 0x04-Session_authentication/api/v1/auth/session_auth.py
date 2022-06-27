#!/usr/bin/env python3
''' create an Authorization class for request verification '''
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    ''' SessionAuth class for more advanced authentication '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        ''' that creates a Session ID for a user_id if user_id is a str

            Args:
                user_id (str): the user_id for the current session

            Returns:
                str: the session id created
        '''
        if user_id and type(user_id) == str:
            sess_id = str(uuid.uuid4())
            self.user_id_by_session_id[sess_id] = user_id
            return sess_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        ''' that returns a User ID based on a Session ID

            Args:
                session_id (str): session id to locate user with

            Returns:
                str: user id for the listed session id
        '''
        return self.user_id_by_session_id.get(session_id) if session_id and \
            type(session_id) == str else None

    def current_user(self, request=None):
        ''' returns a User instance based on a cookie value of the Session's id

            Args:
                request (Flask.Request): the request being sent

            Returns:
                User: instance of the current session's User
        '''
        return User.get(
            self.user_id_for_session_id(self.session_cookie(request))
        )

    def destroy_session(self, request=None):
        ''' deletes the session for the user effectively loging them out

            Args:
                request (Flask.Request): the request sent

            Returns:
                Bool: True if session was deleted, else False
        '''
        if request:
            sess_id = self.session_cookie(request)
            if sess_id:
                u_id = self.user_id_for_session_id(sess_id)
                if u_id:
                    del self.user_id_by_session_id[sess_id]
                    return True
        return False
