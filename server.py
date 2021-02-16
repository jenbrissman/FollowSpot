"""Server for FollowSpot"""

from jinja2 import StrictUndefined
import crud
from model import connect_to_db
from flask import (Flask, jsonify, render_template,
                   request, flash, session, redirect)

app = Flask(__name__)
app.secret_key = "followspot"

########################################################################


@app.route('/')
def show_home():
    """Shows homepage. Lets users with existing accounts login"""

    return render_template('home.html')

#######################################################################


@app.route('/api/register', methods=["POST"])
def register_user():
    """Register a new user"""
    # get users registration information from AJAX
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')

    if crud.check_user(email) != None:
        flash('A user already exists with that email.')
        return jsonify({'status': 'email_error', 'email': email})
    else:
        # add to db crud function
        crud.create_user(first_name, last_name, email, password)
        flash('Your account has been successfully created. Please log in.')
        return jsonify({'first_name': first_name, 'last_name': last_name})

    # user = crud.get_user_by_email(email)
    # user = crud.create_user(first_name, last_name, email, password)
    # if user:
    #
    # else:
    #     crud.create_user(user)
    #     # msg = 'Your account has been successfully created. Please log in.'
    #     flash('Your account has been successfully created. Please log in.')

# return redirect('/', msg=msg)

########################################################################


# @app.route('/register/<user_id>')
# def show_user(user_id):
#     """Show details on a particular user"""

#     user = crud.get_user_by_id(user_id)

#     return render_template('user_details.html', user=user)

########################################################################

# @app.route('/login')
# def login():
#     """Lets users with existing accounts login"""

#     return redirect('/')

########################################################################


@ app.route('/input')
def input():
    """Lets user enter an audition/job"""
    return redirect('/feed')

########################################################################


@ app.route('/feed')
def show_feed():
    """Lets users view and interact with their past entries/inputs"""

########################################################################


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
