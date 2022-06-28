#!/usr/bin/env python3
''' user model from sqlalchemy '''
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sql


Base = declarative_base()


class User(Base):
    ''' user class using sqlalchemy '''
    __tablename__ = 'users'
    # strings may need to be capped at 250
    id = sql.Column(sql.Integer, primary_key=True)
    email = sql.Column(sql.String(250), nullable=False)
    hashed_password = sql.Column(sql.String(250), nullable=False)
    session_id = sql.Column(sql.String(250))
    reset_token = sql.Column(sql.String(250))
