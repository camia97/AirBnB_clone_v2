#!/usr/bin/python3
"""Web Framework"""
from os import abort
from flask import render_template
from ctypes.wintypes import INT
from email.policy import default
from flask import Flask

app = Flask(__name__)
strict_slashes = False


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    return 'C %s' % text.replace("_", " ")


@app.route('/python/<text>')
@app.route('/python/')
def python(text="is cool"):
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>')
def numb(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def index(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_even(n):
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run()
