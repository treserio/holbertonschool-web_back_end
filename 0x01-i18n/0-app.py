#!/usr/bin/env python3
''' temp Flask server
'''
from flask import Flask, render_template, g, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    ''' Root path
    '''
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
