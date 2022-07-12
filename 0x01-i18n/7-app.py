#!/usr/bin/env python3
''' temp Flask server
'''
from flask import Flask, render_template, g, request
from flask_babel import Babel, Locale
import pytz

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
    return render_template('7-index.html')


class Config():
    ''' Config class '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    ''' determine best language to use in order from:

        url parameter: request.args.get('locale'),
        user settings: g.user.get('locale')
        requets headers: request.accept_languages.best_match(app.config)
        default config: app.config['BABEL_DEFAULT_LOCALE']
    '''
    if request.args.get('locale') in Config.LANGUAGES:
        loc = request.args.get('locale')
    elif g.user and g.user.get('locale') in Config.LANGUAGES:
        loc = g.user.get('locale')
    elif request.accept_languages:
        loc = request.accept_languages.best_match(app.config['LANGUAGES'])
    else:
        loc = app.config['BABEL_DEFAULT_LOCALE']
    return loc



def get_user():
    ''' return the mocked user dictionary based on id # '''
    return users[int(request.args.get('login_as'))] \
        if request.args.get('login_as') and \
        int(request.args.get('login_as')) in users else None


@app.before_request
def before_request():
    ''' store the username for the logged in user '''
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    ''' select appropriate timezone for user in order from:

        url parameter: request.args.get('timezone'),
        user settings: g.user.get('timezone')
        default config: app.config['BABEL_DEFAULT_TIMEZONE']
    '''
    if request.args.get('timezone'):
        tz = request.args.get('timezone')
    elif get_user() and get_user().get('timezone'):
        tz = get_user().get('timezone')
    else:
        tz = app.config['BABEL_DEFAULT_TIMEZONE']
    try:
        pytz.timezone(tz)
        return tz
    except pytz.exceptions.UnknownTimeZoneError:
        pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
