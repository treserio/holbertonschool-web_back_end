#!/usr/bin/env python3
''' create an Authorization class for request verification '''
from api.v1.auth.auth import Auth
from base64 import b64decode
import typing as typ


class BasicAuth(Auth):
    ''' BasicAuth class for more advanced authentication '''
    def extract_base64_authorization_header(
        self,
        authorization_header: str
    ) -> str:
        ''' return Base64 part of Authorization header

            Args:
                authorization_header (str): the header with the text to return

            Returns:
                str: everything after 'Basic ' if present in the header text
        '''
        return authorization_header[6:] if type(authorization_header) == str\
            and authorization_header[:6] == 'Basic ' else None

    def decode_base64_authorization_header(
        self,
        base64_authorization_header: str
    ) -> str:
        ''' decode the Base64 string into a utf-8 string

            Args:
                base64_authorization_header (str): the Base64 string

            Returns:
                str: the decoded Base64 string as utf-8
        '''
        try:
            return b64decode(base64_authorization_header).decode('utf-8') \
                if type(base64_authorization_header) == str else None
        except Exception:
            pass

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str
    ) -> typ.Tuple[str, str]:
        ''' returns the user email and password from the Base64 decoded value

            Args:
                decoded_base64_authorization_header (str): string to pull
                values from

            Returns:
                tuple (str, str): (email, password)
        '''
        return (decoded_base64_authorization_header.split(':')[0],
        decoded_base64_authorization_header.split(':')[1])\
            if type(decoded_base64_authorization_header) == str\
            and ':' in decoded_base64_authorization_header else (None, None)
