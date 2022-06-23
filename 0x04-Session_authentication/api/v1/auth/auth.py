#!/usr/bin/env python3
''' create an Authorization class for request verification '''
from flask import request
import typing as typ
import re
import os


class Auth():
    ''' Auth class for api access '''
    def require_auth(
        self,
        path: str,
        excluded_paths: typ.List[str]
    ) -> bool:
        ''' determine if path or path+/ are in the excluded_paths list
            excluded_paths can contain * wildcards now

            Args:
                path (str): string to check
                excluded_paths (list[str]): list of strings that are excluded

            Returns:
                bool: False if the path or path+/ are present else True
        '''
        if path and excluded_paths:
            if re.match('|'.join(
                regX.replace('*', '.*') for regX in excluded_paths
            ), path) or re.match('|'.join(
                regX.replace('*', '.*') for regX in excluded_paths
            ), path+'/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        ''' return the value of the header request Authorization if request &
        request has "Authorization" header

            Args:
                request (Flask.request): the request sent

            Returns:
                str: the Authorization header value
        '''
        return request.headers['Authorization']\
            if request and request.headers.get('Authorization') else None

    def current_user(self, request=None) -> typ.TypeVar('User'):
        ''' unlisted use '''
        return None

    def session_cookie(self, request=None):
        ''' returns a cookie value from a request defined by SESSION_NAME '''
        return request.cookies.get(f"{os.getenv('SESSION_NAME')}") if request \
            else None
