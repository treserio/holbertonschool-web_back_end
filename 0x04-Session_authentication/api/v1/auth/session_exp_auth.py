#!/usr/bin/env python3
''' create an expiring Authorization class for request verification '''
from api.v1.auth.session_auth import SessionAuth
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    ''' Expiring Session Authorization class '''
    def __init__(self):
        ''' new init method '''
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        ''' Create expiring session

            Args:
                user_id (str)
        '''
        sess_id = super().create_session(user_id)
        if sess_id:
            self.user_id_by_session_id[sess_id] = {
                'user_id': user_id,
                'created_at': datetime.now(),
            }
            return sess_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        if session_id and session_id in self.user_id_by_session_id:
            if self.session_duration <= 0:
                return self.user_id_by_session_id[session_id]['user_id']

            if 'created_at' in self.user_id_by_session_id[session_id]:
                c_at = self.user_id_by_session_id[session_id]['created_at']
                if c_at + timedelta(seconds=self.session_duration)\
                        >= datetime.now():
                    return self.user_id_by_session_id[session_id]['user_id']
