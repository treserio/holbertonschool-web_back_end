#!/usr/bin/env python3
''' temp Flask server
'''
from flask import Flask, render_template, g, request
from flask_babel import Babel, Locale


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    ''' Root path
    '''
    return render_template('5-index.html')


class Config():
    ''' Config class '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
# print(app.config)
# print(app.config.__dict__)
# print(app.config['LANGUAGES'])


@babel.localeselector
def get_locale():
    ''' determine best language to use from request.accept_languages '''

    return request.args.get('locale') if request.args.get('locale') \
        in Config.LANGUAGES else \
        request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    ''' return the mocked user dictionary based on id # '''
    return users[int(request.args.get('login_as'))]['name'] \
        if request.args.get('login_as') and \
        int(request.args.get('login_as')) in users else None


@app.before_request
def before_request():
    ''' store the username for the logged in user '''
    g.user = get_user()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
