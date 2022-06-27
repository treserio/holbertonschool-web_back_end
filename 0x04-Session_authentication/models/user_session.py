#!/usr/bin/env python3
''' user_session module
'''
from models.base import Base
from datetime import datetime


class UserSession(Base):
    ''' UserSession class, for storing session data '''
    def __init__(self, *args: list, **kwargs: dict):
        ''' initialize a UserSession instance '''
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
        if kwargs.get('created_at'):
            self.created_at = datetime.strptime(kwargs.get('created_at'),
                "%Y-%m-%dT%H:%M:%S")
        else:
            self.created_at = datetime.now()
        self.save()
