"""Server for FollowSpot"""
from flask import (Flask, jsonify, render_template, request, flash, session, redirect)
from flask_crontab import Crontab
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import os
import psycopg2
from twilio.rest import Client
import cloudinary as Cloud
import cloudinary.uploader
import cloudinary.api
import requests
from werkzeug import secure_filename
from model import connect_to_db, db, User, Audition, Project, Media

app = Flask(__name__)
app.secret_key = "followspot"

twilio_account_sid = os.environ.get('account_sid')
twilio_auth_token = os.environ.get('auth_token')
# messaging_sid = os.environ.get('messaging_service_sid')
cloud_name = os.environ.get('cloud_name')
cloud_api_key = os.environ.get('cloud_api_key')
cloud_api_secret = os.environ.get('cloud_api_secret')

#############################HOME###########################################


@app.route('/')
def show_home():
    """Shows homepage. Lets users with existing accounts login"""

    return render_template('home.html')

#########################CREATE_AN_ACCOUNT#########################################


@app.route('/api/register', methods=["POST"])
def register_user():
    """Register a new user"""
    # get users registration information from AJAX
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    phone = request.form.get('phone')

    if crud.get_user_by_email(email) != None:
        flash('A user already exists with that email.')
        return jsonify({'status': 'email_error', 'email': email})
    else:
        crud.create_user(first_name, last_name, email, password, phone)
        # flash('Your account has been successfully created. Please log in.')
        return jsonify({'first_name': first_name, 'last_name': last_name})

############################LOGIN###########################################


@app.route('/login', methods=['POST'])
def login():

    email = request.form.get('email')
    password = request.form.get('password')

    user_obj = crud.get_user_by_email(email)
    print(user_obj, 'line 66')
    if user_obj != None:
        if password == user_obj.password:
            session['user_id'] = user_obj.user_id
            flash("You are successfully logged in!")
            return redirect('/input')
        else:
            flash('Incorrect password, please try again')
    else:
        flash('You have not created an account with that email. Please create account')
    return redirect('/')

#########################DISPLAY_INPUT_PAGE##############################################


@app.route('/input')
def display_input_page():
    if 'user_id' in session:
        user_id = session['user_id']
        projects = crud.get_projects_by_user(user_id)
        auditions = crud.get_auditions_by_user(user_id)
        n = len(auditions)

        return render_template('input.html', projects=projects, auditions=auditions, n=n)
    return redirect('/')


##########################SUBMIT PROJECT##############################################
@app.route('/submit-project', methods=["POST"])
def submit_project():
    if 'user_id' not in session:
            return redirect("/")
    
    user_id = session['user_id']
    industry = request.json.get('industry')
    project_title = request.json.get('project_title')
    company = request.json.get('company')
    casting_office = request.json.get('casting_office')
    agency = request.json.get('agency')
    
    project = crud.create_project(user_id, industry, project_title,
                            company, casting_office, agency)
    print(project, '*****project*****', 'line108')

    return jsonify({'project_id': project.project_id})    


##########################SUBMIT AUDITION##############################################


@app.route('/submit-audition', methods=["POST"])
def submit_audition():

    if 'user_id' not in session:
        return redirect("/")

    user_id = session['user_id']
    project_id = request.json.get('project_id')
    callback = request.json.get('callback')
    date = request.json.get('date')
    time = request.json.get('time')
    location = request.json.get('location')
    role = request.json.get('role')
    notes = request.json.get('notes')
    
    audition = crud.create_audition(user_id, project_id, callback, date, time, location, role, notes)
    print(audition, '*****audition*****', 'line132')
    # audition_obj = crud.get_audition_by_audition_id(audition.audition_id)

    return jsonify({'audition_id': audition.audition_id})    

#######################SUBMIT MEDIA########################

@app.route('/submit-media', methods=["POST"])
def media():
    if 'user_id' not in session:
        return redirect('/')

    user_id=session['user_id']
    media_url = request.json.get('media_url')
    print(media_url, '********media_url, line146')
    #for file in files uploaded, media_title, f string in the number to match up with where we're at 
    media_title = request.json.get('media_title')
    audition_id = request.json.get('audition_id')

    media_obj = crud.create_media(audition_id, user_id, media_title, media_url)
    print(media_obj, '*****media_obj*****', 'line150')
    return jsonify('success')

#########################FEED PAGE############################################

@app.route('/feed')
def show_feed():
    """Lets users view and interact with their past entries/inputs"""

    if 'user_id' not in session:
        return redirect("/")

    user = crud.get_user_by_id(session['user_id'])
    auditions = crud.get_auditions_by_user(user.user_id)
    auditions = [audition.__dict__ for audition in auditions]
    projects = crud.get_projects_by_user(user.user_id)
    media = crud.get_media_by_user(user.user_id)

    return render_template('feed.html', user=user)

########################################################################

@app.route('/get-auditions')
def get_auditions_by_user():
    """Get projects by user"""
    auditions = {}
    if 'user_id' in session:
        project_id = request.form.get('project_id')
        print("PROJECT ID HERE: ", project_id, 'line 205')
        user_id = session['user_id']
        audition_list = crud.get_auditions_by_project_and_user_id(user_id, project_id)
        print(audition_list, 'line 208')
        auditions["aud"] = audition_list 
        return jsonify(auditions)
    else:
        return redirect('/')

########################################################################

@app.route('/get-callback-info', methods=["POST"])
def get_callback_info():
    if 'user_id' in session:
        user_id = session['user_id']
        project_id = request.json.get('project_id')
        callback_info = crud.get_projects_by_user_and_project_id(user_id, project_id)
        callback_dict = callback_info.__dict__
        callback_dict.pop('_sa_instance_state')

        return jsonify(callback_dict)

########################################################################

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)


 # projs = {}

    # project_ids = [project.project_id for project in projects]
    # print(project_ids, 'line174')
    
    # for project_id in project_ids:
    #     projs[project_id] = {}
    #     project = crud.get_project_by_project_id(project_id)

    #     for audition in project.auditions:
    #         projs[project_id][audition.audition_id] = {}
    #         audition_obj = audition.__dict__
    #         print(audition_obj, '+++++++++AUDITION DICT++++++++++')
    #         projs[project_id][audition.audition_id] = audition_obj

    #         if audition.media:
    #             projs[project_id][audition.audition_id]['media'] = []
    #             for media_obj in audition.media:
    #                 projs[project_id][audition.audition_id]['media'].append((audition.media_obj.media_title, audition.media_obj.link))
            
    # print('+++++++++++++++', projs, 'line191', '*********************')

    # # loop over each project's audition(s) --> for each audition, key = audition.id, value = audition attributes
    # # when we get to looping over media for each audition, audition.media --> append audition.media.url to value = []