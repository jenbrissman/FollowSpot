from model import connect_to_db, db, User, Audition, Project, Media
from datetime import datetime

###########################USER######################################


def create_user(first_name, last_name, email, password, phone):
    """Creates and returns a new user"""

    user = User(first_name=first_name, last_name=last_name,
                email=email, password=password, phone=phone)

    db.session.add(user)
    db.session.commit()

    return user


def check_email(email):
    """Return database row that matches given email."""

    return User.query.filter(User.email == email).first()


def get_user_by_email(email):
    """Return a user by email"""
    return User.query.filter(User.email == email).first()

def get_user_by_phone(phone):
    """Return a user by email"""
    return User.query.filter(User.phone == phone).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def edit_user():
    """Updates a user"""
    pass

def delete_user():
    """Deletes a user"""
    pass


##########################PROJECT#######################################


def create_project(user_id, industry, project_title, company, casting_office, agency):
    """Creates and returns project"""

    project = Project(user_id=user_id, industry=industry, project_title=project_title, company=company,
              casting_office=casting_office, agency=agency)

    db.session.add(project)
    db.session.commit()

    return project


def get_projects_by_user(user_id):

    return Project.query.filter_by(user_id=user_id).all()


def get_projects_by_user_and_project_id(user_id, project_id):
    return Project.query.filter_by(user_id=user_id, project_id=project_id).one()

def get_project_by_project_id(project_id):
    return Project.query.filter_by(project_id=project_id).first()

def edit_project():
    """Updates a user"""
    pass

def delete_project():
    """Deletes a user"""
    pass

############################AUDITION#####################################


def create_audition(user_id, project_id, callback, date, location, role, notes):
    """Creates and returns audition details"""

    audition = Audition(user_id=user_id, project_id=project_id, callback=callback,
                        date=date, location=location, role=role, notes=notes)

    db.session.add(audition)
    db.session.commit()

    return audition

def get_auditions_by_user(user_id):
    return Audition.query.filter_by(user_id=user_id).all()
    # return Audition.query.filter_by(user_id=user_id).order_by(Audition.date.desc()).all()


# def get_auditions_by_date(user_id, date):
#     month = date[5:7]
#     return Audition.query.filter_by(user_id=user_id, date=month).all()


def get_auditions_by_project_and_user_id(user_id, project_id):
    return Audition.query.filter_by(user_id=user_id, project_id=project_id).all()

def get_audition_by_audition_id(audition_id):
    return Audition.query.filter_by(audition_id=audition_id).one()

def get_industry_count(user_id, industry):
    return Audition.query.filter_by(industry=industry).all()


###########################MEDIA#######################################


def create_media(audition_id, user_id, media_title, link):
    """Creates and returns media"""
    media = Media(audition_id=audition_id, user_id=user_id,
                  media_title=media_title, link=link)

    db.session.add(media)
    db.session.commit()

    return media


def get_media_by_user(user_id):

    return Media.query.filter_by(user_id=user_id).all()


def edit_media():
    """Updates a user"""
    pass


def delete_media():
    """Deletes a user"""
    pass


#################################################################

    connect_to_db(app)
    db.create_all()
    print('Connected to db!')
