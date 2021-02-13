from model import User, Audition, Job, Media, connect_to_db, db
from datetime import datetime

#################################################################


def create_user(first_name, last_name, email, password, img_url):
    """creates and returns a new user"""

    user = User(first_name=first_name, last_name=last_name,
                email=email, password=password, img_url=img_url)

    db.session.add(user)
    db.session.commit()

    return user

#################################################################


def create_job(project_title, company, casting_office, agency):
    """creates and returns job"""

    job = Job(project_title=project_title, company=company,
              casting_office=casting_office, agency=agency)

    db.session.add(job)
    db.session.commit()

    return job

#################################################################


def create_audition(industry, callback, role, location, notes, date=datetime.today(), time=datetime.now()):
    """creates and returns audition details"""

    audition = Audition(industry=industry, callback=callback, date=date,
                        time=time, role=role, location=location, notes=notes)

    db.session.add(audition)
    db.session.commit()

    return audition

#################################################################


def create_media(title, link):
    """creates and returns media"""

    media = Media(title=title, link=link)

    db.session.add(media)
    db.session.commit()

    return media


#################################################################

if __name__ == '__main__':
    from server import app
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    db.create_all()
    print('Connected to db!')
