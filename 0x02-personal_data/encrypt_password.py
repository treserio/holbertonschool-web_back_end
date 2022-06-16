#!/usr/bin/env python3
''' module to encrypt passwords '''
import bcrypt


def hash_password(password: str) -> bytes:
    ''' hashes the password string

        Args:
            password (str): the string to encode

        Returns:
            (bytes): the hashed password string
    '''
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    ''' confirms hashed_password matches expected password

        Args:
            hashed_password (bytes): the previously hashed password
            password (str): the string of the unhashed password to check

        Returns:
            bool: true if match, else false
    '''
    return bcrypt.checkpw(password.encode(), hashed_password)
