#!/usr/bin/env python3
''' Write a function called filter_datum that returns the log message
obfuscated '''
import re
import typing as typ
import logging
import os
import mysql.connector as mysqlcon


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    ''' Redacting Formatter class
    '''

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typ.List[str]):
        ''' Instantiates the class using parent classes init method

            Args:
                self: all attributes and methods of the class
                fields: list of keys to obfuscate the values of

            Returns:
                RedactingFormatter object
        '''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        ''' Redact self.fields values from record.msg

            Args:
                self: this object
                record (LogRecord): the log containing the message to redact

            Returns:
                str: the redacted record.msg
        '''
        return filter_datum(
            self.fields,
            self.REDACTION,
            super().format(record),
            self.SEPARATOR
        )


def filter_datum(
        fields: typ.List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    ''' Obfuscate list of values from input string

    Args:
        fields (list): list of keys to obfuscate values of from input string
        redaction (str): the string to use in place of the value
        message (str): the input string to obfuscate
        separator (str): the string used to separate keys:values

    Returns:
        str: the string with field values obfuscated with redaction
    '''
    return re.sub(
        '|'.join(fr'(?<={field}=)[^{separator}]*' for field in fields),
        redaction,
        message
    )


def get_logger() -> logging.Logger:
    ''' Create a Logger obj with a StreamHandler and RedactingFormatter

        Returns:
            Logger with correct settings
    '''
    # logger = logging.getLogger('user_data')
    # logger.setLevel(logging.INFO)
    logger = logging.Logger(name='user_data', level=logging.INFO)
    # set propagate value to False
    logger.propagate = False
    # setup StreamHandler
    logger.addHandler(
        logging.StreamHandler().setFormatter(RedactingFormatter(PII_FIELDS))
    )
    return logger


def get_db() -> mysqlcon.connection.MySQLConnection:
    return mysqlcon.connect(**{
        'host': os.environ.get("PERSONAL_DATA_DB_HOST"),
        'user': os.environ.get("PERSONAL_DATA_DB_USERNAME"),
        'password': os.environ.get("PERSONAL_DATA_DB_PASSWORD"),
        'database': os.environ.get("PERSONAL_DATA_DB_NAME")
    })
