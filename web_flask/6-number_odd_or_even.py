#!/usr/bin/python3
"""Create a flask minimal app"""
from flask import Flask, make_response, render_template
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


@app.route("/number_template/<int:n>", strict_slashes=False)
def first_template(n):
    """Render first template only if n is an integer"""
    context = n
    return render_template("/5-number.html", context=context)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """Check if odd or even number
    Don't escape since it already verifies if type == int
    """
    context = n
    return render_template("/6-number_odd_or_even.html", context=context)


if __name__ == "__main__":
    """Ensure script runs only when called
    debug = True so as to allow reloading of template
    """
    app.run(debug=True, host="0.0.0.0", port=5000)
