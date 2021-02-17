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

    if crud.get_user_by_email(email) != None:
        flash('A user already exists with that email.')
        return jsonify({'status': 'email_error', 'email': email})
    else:
        # add to db crud function
        crud.create_user(first_name, last_name, email, password)
        flash('Your account has been successfully created. Please log in.')
        return jsonify({'first_name': first_name, 'last_name': last_name})

########################################################################


@app.route('/login', methods=['POST'])
def login():
    """Lets users with existing accounts login"""

    email = request.form.get('email')
    password = request.form.get('password')
    # verify with database
    print(email)
    print(password)
    user_obj = crud.get_user_by_email(email)
    print(email)
    print(user_obj.password)
    print(user_obj)
    print('******************')
    if user_obj != None:
        if password == user_obj.password:
            session['email'] = user_obj.email
            flash("You are successfully logged in!")
            return render_template('input.html')
        else:
            flash('Incorrect password, please try again')
    else:
        flash('You have not created an account with that email. Please create account')
    return redirect('/')

########################################################################

# @app.route('/api/login', methods=['POST'])
# def login():
#     """Lets users with existing accounts login"""
#     # grab from ajax
#     email = request.form.get('email')
#     password = request.form.get('password')
#     # verify with database
#     print(email)
#     print(password)
#     user_obj = crud.get_user_by_email(email)
#     print(user_obj)
#     print('******************')
#     if user_obj != None:
#         if password == user_obj.password != None:
#             session['email'] = user_obj.email
#             flash("You are successfully logged in!")
#         else:
#             flash('Incorrect password, please try again')
#     else:
#         flash('You have not created an account with that email. Please create account')

#     return jsonify({'first_name': user_obj.first_name, 'last_name': user_obj.last_name})
#   user_obj is a sqlalchemy object that has keys for each feild (col) you defined for your User class in model
#  sqlalachemy objects are NOT jsonifiable
# therefore we need to create a dictionary that has just strings for keys, and values from that user_obj as values
    # then we send that string (the jsonified dict) to our javascript, it shows up in ajax.js as res
    # res is a plain javascript object, that was created by jQuery reading our jsonified stirng (that was our dict from line 66)
    # res has keys that match the keys we gave our dict from line 66

########################################################################


@ app.route('/input')
def input():
    """Lets user enter an audition/job"""
    return render_template('input.html')

########################################################################


@ app.route('/feed')
def show_feed():
    """Lets users view and interact with their past entries/inputs"""

########################################################################

# @app.route('/register/<user_id>')
# def show_user(user_id):
#     """Show details on a particular user"""

#     user = crud.get_user_by_id(user_id)

#     return render_template('user_details.html', user=user)

########################################################################


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
