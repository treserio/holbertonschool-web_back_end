#!/usr/bin/env python3
''' temp Flask server
'''
from flask import Flask, render_template, g, request
from flask_babel import Babel, Locale, localeselector


app = Flask(__name__)
babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    ''' Root path
    '''
    return render_template('1-index.html')


class Config():
    ''' Config class '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@Babel.localeselector
def get_locale():
    ''' determine best language to use from request.accept_languages '''
    return request.accept_languages.best_match(app.config.LANGUAGES)


app.config.from_object(Config())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
