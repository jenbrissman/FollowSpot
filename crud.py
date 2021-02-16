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


def check_user(email):
    """Return a user by email"""
    return User.query.filter(User.email == email).first()


def verify_user():
    """Verify if a user exists and if password is correct"""
    return User.query.filter(User.password == password).first()


def edit_user():
    """Updates a user"""
    pass


def delete_user():
    """Deletes a user"""
    pass

#################################################################


def create_job(project_title, company, casting_office, agency):
    """Creates and returns job"""

    job = Job(project_title=project_title, company=company,
              casting_office=casting_office, agency=agency)

    db.session.add(job)
    db.session.commit()

    return job


def edit_job():
    """Updates a user"""
    pass


def delete_job():
    """Deletes a user"""
    pass

#################################################################


def create_audition(industry, callback, role, location, notes, date=datetime.today(), time=datetime.now()):
    """Creates and returns audition details"""

    audition = Audition(industry=industry, callback=callback, date=date,
                        time=time, role=role, location=location, notes=notes)

    db.session.add(audition)
    db.session.commit()

    return audition


def edit_audition():
    """Updates a user"""
    pass


def delete_audition():
    """Deletes a user"""
    pass

##################################################################


def create_media(title, link):
    """Creates and returns media"""

    media = Media(title=title, link=link)

    db.session.add(media)
    db.session.commit()

    return media


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
