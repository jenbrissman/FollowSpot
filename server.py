"""Server for FollowSpot"""
from flask import (Flask, jsonify, render_template,
                   request, flash, session, redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "followspot"


@app.route('/')
def homepage():
    """Show the homepage"""

    return render_template('index.html')

# app.route('/newuser')
# app.route('/login')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
