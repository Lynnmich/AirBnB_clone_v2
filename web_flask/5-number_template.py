#!/usr/bin/python3
"""A script that starts a Flask web application & returns various strings"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Returns C plus the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Return Python plus the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Return n if only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Return a HTML page only if n is an integer"""
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
