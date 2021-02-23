"""Server for FollowSpot"""
from flask import (Flask, jsonify, render_template,
                   request, flash, session, redirect)
from model import connect_to_db
import os
import crud
import requests
from jinja2 import StrictUndefined
import psycopg2
# from twilio.rest import Client
import cloudinary as Cloud
import cloudinary
import cloudinary.uploader
import cloudinary.api
from werkzeug import secure_filename

app = Flask(__name__)
app.secret_key = "followspot"

# app.config['UPLOAD_FOLDER'] = "/home/vagrant/src/project/static/img/uploads"
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if request.method == 'POST':

#         if 'files[]' not in request.files:
#             flash('No file part')
#             return redirect(request.url)

#         files = request.files.getlist('files[]')

#         for file in files:
#             if file and allowed_file(file.filename):
#                 filename = secure_filename(file.filename)
#                 file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#         flash('File(s) successfully uploaded')
#         return redirect('/')

# Cloud.config(
#     cloud_name=os.environ['CLOUD_NAME'],
#     api_key=os.environ['API_KEY'],
#     api_secret=os.environ['API_SECRET']
# )
# print(os.environ['CLOUD_NAME'])

# Cloud.config.update = ({
#     'cloud_name': os.environ.get('CLOUDINARY_CLOUD_NAME'),
#     'api_key': os.environ.get('CLOUDINARY_API_KEY'),
#     'api_secret': os.environ.get('CLOUDINARY_API_SECRET')
# })

cloud_name = os.environ.get('cloud_name')
cloud_api_key = os.environ.get('cloud_api_key')
cloud_api_secret = os.environ.get('cloud_api_secret')


print(cloud_name, "***************************************")
print(cloud_api_key, "***************************************")
print(cloud_api_secret, "***************************************")
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

    if crud.get_user_by_email(email) != None:
        flash('A user already exists with that email.')
        return jsonify({'status': 'email_error', 'email': email})
    else:
        crud.create_user(first_name, last_name, email, password)
        # flash('Your account has been successfully created. Please log in.')
        return jsonify({'first_name': first_name, 'last_name': last_name})

############################LOGIN###########################################


@app.route('/login', methods=['POST'])
def login():

    email = request.form.get('email')
    password = request.form.get('password')

    user_obj = crud.get_user_by_email(email)
    print(user_obj)
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
        jobs = crud.get_jobs_by_user(user_id)
        auditions = crud.get_auditions_by_user(user_id)
        n = len(auditions)

        return render_template('input.html', jobs=jobs, auditions=auditions, n=n)

##########################INPUT_AUDITION##############################################


@app.route('/input', methods=["POST"])
def input():
    """Lets user enter an audition/job/ also media?"""

    if 'user_id' not in session:
        return redirect("/")

    my_cloudinary = cloudinary.config(
        cloud_name=cloud_name,
        api_key=cloud_api_key,
        api_secret=cloud_api_secret
    )

    print('*'*20, '\n')
    print(request.form, request.form.keys())
    print('*'*20, '\n')

    user_id = session['user_id']
    industry = request.form.get('industry')
    project_title = request.form.get('project_title')
    company = request.form.get('company')
    casting_office = request.form.get('casting_office')
    agency = request.form.get('agency')

    callback = request.form.get('callback')
    date = request.form.get('date')
    time = request.form.get('time')
    location = request.form.get('location')
    role = request.form.get('role')
    notes = request.form.get('notes')

    # media_title = request.files['pic']
    # media_title = request.files.get('pic')
    # cloudinary_upload = cloudinary.uploader.upload(media_title)
    # link = cloudinary_upload['url']

    media_title = request.form.get('media_title')
    link = request.form.get('link')

    job = crud.create_job(user_id, industry, project_title,
                          company, casting_office, agency)
    audition = crud.create_audition(
        user_id, job.job_id, callback, date, time, location, role, notes)
    media = crud.create_media(
        audition.audition_id, user_id, media_title, link)
    return redirect('/feed')

###########################DISPLAY_FEED#############################################


# @app.route('/feed')
# def display_input_page():
#     return render_template('feed.html')


#########################FEED PAGE############################################
@ app.route('/feed')
def show_feed():
    """Lets users view and interact with their past entries/inputs"""

    if 'user_id' not in session:
        return redirect("/")
    # else:
    #     return redirect("/feed")

    user = crud.get_user_by_id(session['user_id'])
    auditions = crud.get_auditions_by_user(user.user_id)
    jobs = crud.get_jobs_by_user(user.user_id)
    media = crud.get_media_by_user(user.user_id)
    # import pdb
    # pdb.set_trace()
    return render_template('feed.html', auditions=auditions, user=user, jobs=jobs, media=media)


########################################################################

@app.route('/get-auditions')
def get_auditions_by_user():
    """Get jobs by user"""

    if 'user_id' in session:
        job_id = request.form.get('job_id')
        user_id = session['user_id']
        auditions = crud.get_auditions_by_job_and_user_id(user_id, job_id)
        return jsonify(auditions)
    else:
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
