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
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user_list = User.search({'email': email})
    print(len(user_list))
    if not user_list:
        return jsonify({"error": "no user found for this email"}), 404
    if not user_list[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    output = jsonify(user_list[0].to_json())
    output.set_cookie(
        os.getenv('SESSION_NAME'),
        auth.create_session(user_list[0].id)
    )
    return output


@app_views.route(
    '/auth_session/logout',
    methods=['DELETE'],
    strict_slashes=False
)
def logout():
    ''' delete a user session to effectively log them out '''
    from api.v1.app import auth
    return jsonify({}), 200 if auth.destroy_session(request) else abort(404)
