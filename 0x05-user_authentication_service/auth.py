#!/usr/bin/env python3
''' authentication module '''
import bcrypt as bc


def _hash_password(password: str) -> bytes:
    ''' a salted hash of the input password, hashed with bcrypt.hashpw.

        Args:
            password (str): the string to hash

        Returns:
            bytes: the byte representation of the input string
    '''
    return bc.hashpw(password.encode(), bc.gensalt(9))


