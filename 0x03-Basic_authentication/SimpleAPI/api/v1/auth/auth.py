from flask import request
import typing as typ

class Auth():
    ''' Auth class for api access '''
    def require_auth(
        self,
        path: str,
        excluded_paths: typ.List[str]
        ) -> bool:
        ''' unlisted use '''
        return False


    def authorization_header(self, request=None) -> str:
        ''' unlisted use '''
        return None


    def current_user(self, request=None) -> typ.TypeVar('User'):
        ''' unlisted use '''
        return None
