from jinja2 import StrictUndefined
import crud
from model import connect_to_db
from flask import (Flask, jsonify, render_template,
                   request, flash, session, redirect)

"""Server for FollowSpot"""

app = Flask(__name__)
app.secret_key = "followspot"

########################################################################


@app.route('/')
def homepage():
    """Show the homepage"""

    return render_template('home.html')

########################################################################


@app.route('/user', methods=['POST'])
def create_user():
    """create a new user"""
    first_name = request.args.get['first_name']
    last_name = request.args.get['last_name']
    email = request.args.get['email']
    password = request.args.get['password']
    img_url = request.args.get['img_url']

    user = crud.get_user_by_email('email')
    if user:
        flash('A user already exists with that email.')
    else:
        crud.create_user(first_name, last_name, email, password)
        flash('Your account has been successfully created. Please log in.')

    return render_template('user.html')

########################################################################


@app.route('/login')
def login():
    """let users with existing accounts login"""
    return render_template('login.html')

    # return redirect('/input')

########################################################################


@app.route('/input')
def input():
    """lets user enter an audition/job"""
    return redirect('/feed')

########################################################################


@app.route('/feed')
def show_feed():
    """lets users view and interact with their past entries/inputs"""

########################################################################


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
