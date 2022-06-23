#!/usr/bin/env python3
""" Module of session_auth views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route(
    '/auth_session/login',
    methods=['POST'],
    strict_slashes=False
)
def login():
    ''' session authentication handeler '''
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({ "error": "email missing" }), 400
    if not password:
        return jsonify({ "error": "password missing" }), 400

    cu = User.search({'email': email})

    if not cu:
        return jsonify({ "error": "no user found for this email" }), 404
    if not cu[0].is_valid_password(password):
        return jsonify({ "error": "wrong password" }), 401

    from api.v1.app import auth
    auth.create_session(cu[0].id)
    output = jsonify(cu[0].to_json())
    output.set_cookie(os.getenv('SESSION_NAME'), cu[0].id)
    return output
