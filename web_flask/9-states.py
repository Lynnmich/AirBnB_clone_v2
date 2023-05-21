#!/usr/bin/python3
"""A script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    states = storage.all("State").values()
    return render_template('7-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_cities(id):
    state = storage.get("State", id)
    if state is None:
        return render_template('9-not_found.html')
    else:
        return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
