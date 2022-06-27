#!/usr/bin/env python3
''' use expiring Authorization class to create a version stored in db '''
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


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
        UserSess = UserSession(**{
            'user_id': user_id,
            'session_id': super().create_session(user_id),
        })
        UserSess.save()
        return UserSess.session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        ''' that returns the User ID by requesting UserSession in the database
            based on session_id

            Args:
                session_id (str): the session id for the user needed

            Returns:
                str: the user's id from the requested session
        '''
        if session_id and session_id in self.user_id_by_session_id:
            if self.session_duration <= 0:
                return self.user_id_by_session_id[session_id]['user_id']

            if 'created_at' in self.user_id_by_session_id[session_id]:
                c_at = self.user_id_by_session_id[session_id]['created_at']
                if c_at + timedelta(seconds=self.session_duration)\
                        >= datetime.now():
                    UserSess_list = UserSession.search({
                        'session_id': session_id
                    })
                    if len(UserSess_list) > 0:
                        return UserSess_list[0].user_id

    def destroy_session(self, request=None):
        ''' that destroys the UserSession based on the Session ID from the
            request cookie

            Args:
                request (Flask.Request): the request sent
        '''
        # print('sessions', self.user_id_by_session_id)
        # print('cookie', self.session_cookie(request))
        # print()
        UserSess_list = UserSession.search({
            'session_id': self.session_cookie(request)
        })
        # print('usrList', UserSess_list)
        if super().destroy_session(request):
            UserSess_list[0].remove()
            return True
        return False
