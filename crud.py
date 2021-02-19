from model import connect_to_db, db, User, Audition, Job, Media
from datetime import datetime

#################################################################


def create_user(first_name, last_name, email, password):
    """Creates and returns a new user"""

    user = User(first_name=first_name, last_name=last_name,
                email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def get_user_by_email(email):
    """Return a user by email"""
    return User.query.filter(User.email == email).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def edit_user():
    """Updates a user"""
    pass


def delete_user():
    """Deletes a user"""
    pass

#################################################################


def create_job(user_id, industry, project_title, company, casting_office, agency):
    """Creates and returns job"""

    job = Job(user_id=user_id, industry=industry, project_title=project_title, company=company,
              casting_office=casting_office, agency=agency)

    db.session.add(job)
    db.session.commit()

    return job


def get_jobs_by_user(user_id):

    return Job.query.filter_by(user_id=user_id).all()


def edit_job():
    """Updates a user"""
    pass


def delete_job():
    """Deletes a user"""
    pass

#################################################################


def create_audition(user_id, job_id, callback, date, time, location, role, notes):
    """Creates and returns audition details"""

    audition = Audition(user_id=user_id, job_id=job_id, callback=callback,
                        date=date, time=time, location=location, role=role, notes=notes)

    db.session.add(audition)
    db.session.commit()

    return audition


def get_auditions_by_user(user_id):

    return Audition.query.filter_by(user_id=user_id).all()

##################################################################


def create_media(media_title, link):
    """Creates and returns media"""

    media = Media(media_title=media_title, link=link)

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


if __name__ == '__main__':
    from server import app
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    db.create_all()
    print('Connected to db!')
