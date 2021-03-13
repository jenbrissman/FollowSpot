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

####################################HOME###########################################

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

######################################LOGIN###########################################

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

################################INPUT PAGE##############################################

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

###############################SUBMIT PROJECT##############################################

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
    location = request.json.get('location')
    role = request.json.get('role')
    notes = request.json.get('notes')
    
    audition = crud.create_audition(user_id, project_id, callback, date, location, role, notes)

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
    return jsonify({'completed': True})

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

###########################TEXT AUDITION DETAILS######################################

#     @app.route('/send-audition-details')
#     def create_audition_notification():
#     """Get projects by user"""
#     auditions = {}
#     id = params.id

#     if 'user_id' in session:
#         project_id = request.form.get('project_id')
#         user_id = session['user_id']
#         audition = crud.get_auditions_by_audition_id(audition_id)
#         # send text here
#         twilio_client = TC
#         audition_text = """
#             Check out my audition on follow spot http://localhost:3001/audtions/{}
#         """.format(audition.audition_id)
#         twilio_client.send_sms(audition_text)
#         return jsonify(auditions)


#     # link button href = localhost:3001/auditions/123
#     @app.route('/auditions/<id>')
#     def get_auditions_by_id(id):
#     """Get projects by user"""
#     auditions = {}
#     id = params.id

#     if 'user_id' in session:
#         project_id = request.form.get('project_id')
#         user_id = session['user_id']
#         audition_list = crud.get_auditions_by_project_and_user_id(user_id, id)
#         auditions["aud"] = audition_list 
#         # send text here
#         twilio_client = TC
#         audition_text = """
#             {0}, {}
#         """.format(audition.name)
#         twilio_client.send_sms(audition_text)
#         return jsonify(auditions)
#     else:
#         return redirect('/')

# @app.route('/get-auditions')
# def get_auditions_by_user():
#     """Get projects by user"""
#     auditions = {}
#     if 'user_id' in session:
#         project_id = request.form.get('project_id')
#         user_id = session['user_id']
#         audition_list = crud.get_auditions_by_project_and_user_id(user_id, project_id)
#         auditions["aud"] = audition_list 
#         return jsonify(auditions)
#     else:
#         return redirect('/')

##############################CALLBACK INFO####################################################

@app.route('/get-callback-info', methods=["POST"])
def get_callback_info():
    if 'user_id' in session:
        user_id = session['user_id']
        project_id = request.json.get('project_id')
        callback_info = crud.get_projects_by_user_and_project_id(user_id, project_id)
        callback_dict = callback_info.__dict__
        callback_dict.pop('_sa_instance_state')

        return jsonify(callback_dict)

###################################CHARTS#################################################

@app.route('/charts')
def view_charts():
    if 'user_id' in session:
        user = crud.get_user_by_id(session['user_id'])

        return render_template('chart.html', user=user)


############################AUDITION CHART#################################################

@app.route('/audition-chart.json')
def get_auditions_total():

    if 'user_id' in session:

        user = crud.get_user_by_id(session['user_id'])
        auditions = crud.get_auditions_by_user(user.user_id)
        # print(auditions[0].date.strftime("%B"), "**************line253*********")
        # print(type(auditions[0].date), "**************line253*********")

        years = {}

        for audition in auditions:
            year = audition.date.strftime("%Y")
            month = audition.date.strftime("%B")
            if year not in years:
                years[year] = {"January" : 0, 
                                "February" : 0,
                                "March" : 0,
                                "April" : 0,
                                "May" : 0,
                                "June" : 0,
                                "July" : 0,
                                "August" : 0,
                                "September" : 0,
                                "October" : 0,
                                "November" : 0,
                                "December" : 0}
            years[year][month] += 1
        
        # print(years, "*********line296kat******")
        data = {}

        datasets = []
        for year_name in years:
            year_dict = years[year_name]
            # print(f"year is {year_name} in the year loop. year. ")
            datasets.append({
                    "label": year_name,
                    "data": list(year_dict.values())
                })

        data["months"] = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        data["datasets"] = datasets
        # print(f"\n\nDATA IS {data}, \n{data['months']}")
        return jsonify(data)

############################INDUSTRY CHART#################################################

@app.route('/industry-chart.json')
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


############################AGENCY CHART############################################

@app.route('/agency-chart.json')
def get_agency_totals():


    if 'user_id' in session:
    
        user = crud.get_user_by_id(session['user_id'])
        auditions = crud.get_auditions_by_user(user.user_id)
        agency_labels = []
        audition_counts = {}

        for audition in auditions:
            if audition.project.agency not in agency_labels:
                agency_labels.append(audition.project.agency)
            audition_counts[audition.project.agency]=audition_counts.get(audition.project.agency, 0)+1

        data = {'labels': agency_labels , 'values' : list(audition_counts.values()) }

        return jsonify(data) 

        
#################################LOGOUT###################################################

@app.route('/logout')
def logout():
    print(session)
    if session['user_id']:
        session.pop('user_id')
        return redirect('/')
    else: 
        pass


# session.clear()


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
