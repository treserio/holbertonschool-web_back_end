#!/usr/bin/env python3
''' create an Authorization class for request verification '''
from flask import request
import typing as typ


class Auth():
    ''' Auth class for api access '''
    def require_auth(
        self,
        path: str,
        excluded_paths: typ.List[str]
    ) -> bool:
        ''' determine if path or path+/ are in the excluded_paths list

            Args:
                path (str): string to check
                excluded_paths (list[str]): list of strings that are excluded

            Returns:
                bool: False if the path or path+/ are present else True
        '''
        return not (path in excluded_paths or f'{path}/' in excluded_paths)\
            if path else True

    def authorization_header(self, request=None) -> str:
        ''' unlisted use '''
        return request.headers['Authorization']\
            if request and request.headers.get('Authorization') else None

    def current_user(self, request=None) -> typ.TypeVar('User'):
        ''' unlisted use '''
        return None
