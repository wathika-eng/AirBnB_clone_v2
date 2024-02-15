#!/usr/bin/python3
"""Create a flask minimal app"""
from flask import Flask, make_response
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Test if working"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """GET a response HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    """Gets value of a text"""
    text = escape(text.replace("_", " "))
    return f"C {escape(text)}"


@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text="is cool"):
    """Default val python is cool"""
    text = escape(text.replace("_", " "))
    return f"Python {escape(text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def if_number(n):
    """Display n if a number"""
    return f"{escape(n)} is a number"


if __name__ == "__main__":
    """Ensure script runs only when called"""
    app.run(host="0.0.0.0", port=5000)
