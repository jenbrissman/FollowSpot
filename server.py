"""Server for FollowSpot"""
from flask import (Flask, jsonify, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import os
import psycopg2
from datetime import datetime
from twilio.rest import Client
import cloudinary as Cloud
import cloudinary.uploader
import cloudinary.api
import requests
from werkzeug import secure_filename
from model import connect_to_db, db, User, Audition, Project, Media

app = Flask(__name__)
app.secret_key = "followspot"

twilio_account_sid = os.environ.get('twilio_account_sid')
twilio_auth_token = os.environ.get('twilio_auth_token')
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

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    phone = request.form.get('phone')

    if crud.get_user_by_email(email) != None:
        return jsonify({'status': 'email_error', 'email': email})
    else:
        crud.create_user(first_name, last_name, email, password, phone)
        client = Client(twilio_account_sid, twilio_auth_token)
        message = client.messages \
                    .create(
                        body="Hello from FollowSpot",
                        from_="+16505501808",
                        to=request.form.get('phone'))

        return jsonify({'first_name': first_name, 'last_name': last_name})

############################LOGIN###########################################

@app.route('/login', methods=['POST'])
def login():

    email = request.form.get('email')
    password = request.form.get('password')

    user_obj = crud.get_user_by_email(email)
    
    if user_obj != None:
        if password == user_obj.password:
            session['user_id'] = user_obj.user_id
            # client = Client(twilio_account_sid, twilio_auth_token)
            # message = client.messages \
            #         .create(
            #             body="Hello from FollowSpot",
            #             from_="+16505501808",
            #             to=crud.get_user_by_phone(phone))
            return redirect('/input')
        else:
            flash('Incorrect password, please try again')
    else:
        flash('You have not created an account with that email. Please create account')
    return redirect('/')

# @app.route('/api/login', methods=['POST'])
# def login():

#     email = request.form.get('login_email')
#     password = request.form.get('login_password')
#     user_by_email = crud.get_user_by_email(email)

#     if user_by_email != None and user_by_email.password == password:
#         session['user_id'] = user_by_email.user_id
#         return jsonify({'status': 'ok', 'login_email': login_email, 'login_password': login_password})
#     else:
#         return jsonify({'status': 'error', 'msg': 'Not registered. Please create an account.'})

#########################DISPLAY_INPUT_PAGE##############################################

@app.route('/input')
def display_input_page():
    if 'user_id' in session:
        user_id = session['user_id']
        projects = crud.get_projects_by_user(user_id)
        auditions = crud.get_auditions_by_user(user_id)
        user = crud.get_user_by_id(session['user_id'])
        n = len(auditions)

        return render_template('input.html', projects=projects, auditions=auditions, user=user, n=n)
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

    return jsonify({'audition_id': audition.audition_id})    

#######################SUBMIT MEDIA####################################################

@app.route('/submit-media', methods=["POST"])
def media():
    if 'user_id' not in session:
        return redirect('/')

    user_id=session['user_id']
    media_url = request.json.get('media_url')
    media_title = request.json.get('media_title')
    audition_id = request.json.get('audition_id')

    media_obj = crud.create_media(audition_id, user_id, media_title, media_url)
    return jsonify('success')

#########################FEED PAGE####################################################

@app.route('/feed')
def show_feed():
    """Lets users view and interact with their past entries/inputs"""

    if 'user_id' not in session:
        return redirect("/")

    user = crud.get_user_by_id(session['user_id'])
    auditions = crud.get_auditions_by_user(user.user_id)
    projects = crud.get_projects_by_user(user.user_id)
    media = crud.get_media_by_user(user.user_id)
    
    return render_template('feed.html', user=user)

##################################################################################

@app.route('/get-auditions')
def get_auditions_by_user():
    """Get projects by user"""
    auditions = {}
    if 'user_id' in session:
        project_id = request.form.get('project_id')
        user_id = session['user_id']
        audition_list = crud.get_auditions_by_project_and_user_id(user_id, project_id)
        auditions["aud"] = audition_list 
        return jsonify(auditions)
    else:
        return redirect('/')

##################################################################################

@app.route('/get-callback-info', methods=["POST"])
def get_callback_info():
    if 'user_id' in session:
        user_id = session['user_id']
        project_id = request.json.get('project_id')
        callback_info = crud.get_projects_by_user_and_project_id(user_id, project_id)
        callback_dict = callback_info.__dict__
        callback_dict.pop('_sa_instance_state')

        return jsonify(callback_dict)

############################CHARTS#################################################

@app.route('/charts')
def view_charts():
    if 'user_id' in session:
        user = crud.get_user_by_id(session['user_id'])

        return render_template('chart.html', user=user)


############################CHARTS1#################################################

@app.route('/charts.json')
def get_industry_total():

    if 'user_id' in session:
    
        user = crud.get_user_by_id(session['user_id'])
        auditions = crud.get_auditions_by_user(user.user_id)
        aud_industry_labels = []
        aud_industry_counts = {}

        for audition in auditions:
            if audition.project.industry not in aud_industry_labels:
                aud_industry_labels.append(audition.project.industry)
            aud_industry_counts[audition.project.industry]=aud_industry_counts.get(audition.project.industry, 0)+1

        data = {'labels': aud_industry_labels , 'values' : list(aud_industry_counts.values()) }

        return jsonify(data)

############################CHARTS2#################################################

# @app.route('/charts2.json')
# def get_auditions_total():

    # if 'user_id' in session:
    
    #     user = crud.get_user_by_id(session['user_id'])
    #     auditions = crud.get_auditions_by_user(user.user_id)
    #     date = crud.get_auditions_by_date(user.user_id, date)

    #     audition_months = [] # holds 12 months in string format

    #     now = datetime.now() # this exact moment as a date object
    #     now_str = now.strftime('%B') # this exact month as a string (mar)

    #     for month in range(12): #loops over past 12 months
    #         month = now_str #mar
    #         # dater = str(date.month) 
    #         audition_months.append(month) #mar
    #         month = month - timedelta(months=1) # first iteration = feb, jan
            
    #     print('!!!!!!!\n!!!!\n!!!!!\n!!!!!\n!!!!')
    #     print(audition_months)

        # months_2020 = ["Jan", "Feb", "Mar", etc]
        # audition_nums = [5, 6, 10, et]
        # new_lst = []

        # new_list = [("Jan", 5), ("Feb", 6), ("Mar", 10)]

        # y_axis = [("jan", 5), ("feb", 6), ("March", 10), ("April", 4), ("May", 2), ("June", 4), ("July", 6), ("August", 8), ("September", 5), ("October", 12), ("November", 4), ("December", 10)]
        # x_axis = ["January", "February", "Mach", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

        # data = { "months": x_axis, "audition": y_axis }

        # data = {}
        # data["months"] = ["January", "February", "Mach", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        # data["auditions"] = [5, 6, 10, 4, 2, 1, 6, 8, 5, 12, 4, 7]

        # return jsonify(data)

#################################LOGOUT###################################################

@app.route('/logout')
def logout():
    print(session)
    if session['user_id']:
        session.pop('user_id')
        flash('You are logged out, byeeeee')
        return redirect('/')
    else: 
        pass


# session.clear()


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
