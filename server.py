from jinja2 import StrictUndefined
import crud
from model import connect_to_db
from flask import (Flask, jsonify, render_template,
                   request, flash, session, redirect)
"""Server for FollowSpot"""


app = Flask(__name__)
app.secret_key = "followspot"


@app.route('/')
def homepage():
    """Show the homepage"""

    return render_template('homepage.html')


@app.route('/register', methods=['POST'])
def register_user():
    """create a new user"""
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']

    user = crud.get_user_by_email('email')
    if user:
        flash('A user already exists with that email.')
    else:
        crud.create_user(first_name, last_name, email, password)
        flash('Your account has been successfully created. Please log in.')

        return redirect('/')


@app.route('/login')
def login():
    """let users with existing accounts login"""
    return render_template('login.html')

    # return redirect('/input')


@app.route('/input')
def input():
    """lets user enter an audition/job"""
    return redirect('/feed')


@app.route('/feed')
def show_feed():
    """lets users view and interact with their past entries/inputs"""


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
