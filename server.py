"""Server for FollowSpot"""
from flask import (Flask, jsonify, render_template,
                   request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import psycopg2

app = Flask(__name__)
app.secret_key = "followspot"

#############################HOME###########################################


@app.route('/')
def show_home():
    """Shows homepage. Lets users with existing accounts login"""

    return render_template('home.html')

############################LOGIN###########################################


@app.route('/login', methods=['POST'])
def login():
    """Lets users with existing accounts login"""

    email = request.form.get('email')
    password = request.form.get('password')

    user_obj = crud.get_user_by_email(email)

    if user_obj != None:
        if password == user_obj.password:
            session['user_id'] = user_obj.user_id
            flash("You are successfully logged in!")
            return render_template('input.html')
        else:
            flash('Incorrect password, please try again')
    else:
        flash('You have not created an account with that email. Please create account')
    return redirect('/')

#########################CREATE_AN_ACCOUNT#########################################


@app.route('/api/register', methods=["POST"])
def register_user():
    """Register a new user"""
    # get users registration information from AJAX
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')

    # user_obj = crud.get_user_by_email(email)

    # if user_obj != None:
    #     if password == user_obj.password:
    #         session['email'] = user_obj.email
    #         flash("You are successfully logged in!")
    #         return render_template('feed.html')
    #     else:
    #         flash('Incorrect password, please try again')
    # else:
    #     flash('You have not created an account with that email. Please create account')
    # return redirect('/')

    if crud.get_user_by_email(email) != None:
        flash('A user already exists with that email.')
        return jsonify({'status': 'email_error', 'email': email})
    else:
        # add to db crud function
        crud.create_user(first_name, last_name, email, password)
        flash('Your account has been successfully created. Please log in.')
        return jsonify({'first_name': first_name, 'last_name': last_name})

##########################INPUT_AUDITION##############################################


@ app.route('/input', methods=["POST"])
   if 'user_id' not in session:
        return redirect("/")


def input():
    """Lets user enter an audition/job"""
    callback = request.form.get('callback')
    industry = request.form.get('industry')
    date = request.form.get('date')
    time = request.form.get('time')
    project_title = request.form.get('project_title')
    company = request.form.get('company')
    role = request.form.get('role')
    casting_office = request.form.get('casting_office')
    agency = request.form.get('agency')
    location = request.form.get('location')
    notes = request.form.get('notes')
    media_title = request.form.get('media_title')
    link = request.form.get('link')

    job = crud.create_job(project_title, industry,
                          company, casting_office, agency)
    media = crud.create_media(title, link)
    audition = crud.create_audition(
        callback, date, time, role, location, notes)

    return render_template('input.html', job=job, media=media, audition=audition)


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


@ app.route('/feed')
def show_feed():


"""Lets users view and interact with their past entries/inputs"""

   if 'user_id' not in session:
        return redirect("/")
    # get user (by email?)
    # get auditions by user_id
    # audition.user.user_id or

    if 'user_id' not in session:
        redirect("/")

    user = crud.get_user_by_id(session['user_id'])
    auditions = crud.get_auditions_by_user(user.user_id)

    return render_template('feed.html', auditions=auditions)


########################################################################

# @app.route('/register/<user_id>')
# def show_user(user_id):
#     """Show details on a particular user"""

    # if 'user_id' not in session:
    #     return redirect("/")

#     user = crud.get_user_by_id(user_id)

#     return render_template('user_details.html', user=user)

########################################################################


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
