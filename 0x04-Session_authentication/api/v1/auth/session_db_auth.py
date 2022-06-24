#!/usr/bin/env python3
''' use expiring Authorization class to create a version stored in db '''
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    ''' session expiring db stored auth class '''
    def create_session(self, user_id: str = None) -> str:
        ''' creates and stores instance of UserSession and returns
            Session ID

            Args:
                user_id (str): the user id to use generating UserSession

            Returns:
                str: the new user's id
        '''
        UserSess = UserSession(
            user_id=user_id,
            session_id=super().create_session(user_id)
        )
        UserSess.save()
        return UserSess.session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        ''' that returns the User ID by requesting UserSession in the database
            based on session_id
        '''
        UserSession.get(super().user_id_for_session_id(session_id))
        return UserSession.user_id

    def destroy_session(self, request=None):
        ''' that destroys the UserSession based on the Session ID from the
            request cookie

            Args:
                request (Flask.Request): the request sent
        '''
        UserSess = UserSession.get(
            self.user_id_by_session_id(self.session_cookie(request))
        )
        self.destroy_session(UserSess.session_id)
        UserSess.remove()
