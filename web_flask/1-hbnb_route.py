#!/usr/bin/python3
"""Web Framework"""
from flask import Flask

app = Flask(__name__)
strict_slashes = False


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


if __name__ == '__main__':
    app.run()
