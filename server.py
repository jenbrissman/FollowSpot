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
        flash('Your account has been successfully created. Please log in.')
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

        print(jobs)
        print(auditions)
        print(type(auditions))
        return render_template('input.html', jobs=jobs, auditions=auditions, n=n)

##########################INPUT_AUDITION##############################################


@app.route('/input', methods=["POST"])
def input():
    """Lets user enter an audition/job"""

    if 'user_id' not in session:
        return redirect("/")

    user_id = session['user_id']
    print(user_id)
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

    # media_title = request.form.get('media_title')
    # link = request.form.get('link')

    job = crud.create_job(user_id, industry, project_title,
                          company, casting_office, agency)
    # media = crud.create_media(audition_id, user_id, media_title, link)
    audition = crud.create_audition(
        user_id, job.job_id, callback, date, time, location, role, notes)
    return jsonify('success')
    # return jsonify({'job': job, 'media': media, 'audition': audition})
    # return render_template('input.html', job=job, media=media, audition=audition)
    # return jsonify({'industry': industry, 'project_title': project_title, 'company': company, 'casting_office': casting_office, 'agency': agency, 'callback': callback, 'date': date, 'time': time, 'location': location, 'role': role, 'notes': notes, 'media_title': media_title, 'link': link})

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


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
