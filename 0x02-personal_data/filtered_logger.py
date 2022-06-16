#!/usr/bin/env python3
''' Write a function called filter_datum that returns the log message
obfuscated '''
import re


def filter_datum(
        fields: list,
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    ''' Obfuscate list of values from input string

    Parameters:
        fields (list): list of keys to obfuscate values of from input string
        redaction (str): the string to use in place of the value
        message (str): the input string to obfuscate
        separator (str): the string used to separate keys:values

    Returns:
        str: the string with field values obfuscated with redaction
    '''
    return re.sub(
        '|'.join(fr'(?<={field}=)[^{separator}]+' for field in fields),
        redaction,
        message
    )
