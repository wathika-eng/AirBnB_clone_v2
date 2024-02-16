#!/usr/bin/python3
"""List states from storage"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def get_states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda s: s.name)
    return render_template("/7-states_list.html", states=sorted_states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
