#!/usr/bin/env python3
''' temp Flask server
'''
from flask import Flask, Response, request, jsonify, abort, redirect
from user import User
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    ''' Root path
    '''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user() -> User:
    ''' Registering a user
    JSON body:
        - email
        - password
        - session_id (optional)
        - reset_token (optional)
    Return:
        - User object JSON representation
        - 400 if user is already registered
    '''
    try:
        res_data = request.form
        if {'email', 'password'}.issubset(set(res_data)):
            AUTH.register_user(**res_data)
            return jsonify({
                'email': res_data['email'],
                'message': 'user created',
            })
        return jsonify({'message': 'values missing, email & password'}), 400
    except Exception:
        return jsonify({'message': 'email already registered'}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login_user() -> Response:
    ''' logging in user with valid email / password
    JSON body:
        - email
        - password
    Return:
        - Session ID cookie in response with JSONed form
        - 401 if login info is invalid
    '''
    if AUTH.valid_login(request.form['email'], request.form['password']):
        res = jsonify({
            "email": f"{request.form['email']}",
            "message": "logged in"
        })
        res.set_cookie(
            'session_id',
            AUTH.create_session(request.form['email'])
        )
        return res
    abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout_user() -> Response:
    ''' set User's session_id to None, logging out
    JSON body:
        - session_id
    Return:
        - redirect to '/' if user exists
        - 403 if the user doesn't exist
    '''
    try:
        AUTH.destroy_session(request.cookies['session_id'])
        return redirect('/')
    except Exception:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile_user() -> Response:
    ''' find the email of the user tied to the session id sent
    JSON body:
        - session_id
    Return:
        - JSON response with the user's email
        - 403 if the user doesn't exist
    '''
    try:
        user = AUTH.get_user_from_session_id(request.cookies['session_id'])
        res = jsonify({"email": user.email})
        res.set_cookie(
            'session_id',
            user.session_id
        )
        return res
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def reset_pw() -> Response:
    ''' generate reset_password token for user
    JSON body:
        - email
    Return:
        - JSON response with the user's email and reset_token
        - 403 if the user doesn't exist
    '''
    try:
        user = AUTH._db.find_user_by(email=request.form['email'])
        return jsonify({
            "email": user.email,
            "reset_token": AUTH.get_reset_password_token(user.email)
        })
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
