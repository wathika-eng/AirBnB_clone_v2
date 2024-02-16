#!/usr/bin/python3
"""Create a flask minimal app"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Test if working"""
    return "Hello HBNB!"


if __name__ == "__main__":
    """Ensure script runs only when called"""
    app.run(debug=True, host="0.0.0.0", port=5000)
