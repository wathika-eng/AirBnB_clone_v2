#!/usr/bin/python3
"""Create a flask minimal app"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Test if working"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """GET a response HBNB"""
    return "HBNB"


if __name__ == "__main__":
    """Ensure script runs only when called"""
    app.run(host="0.0.0.0", port=5000)
