from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

########################################################################
# User has many auditions
# Auditions can have one job/A job can have many auditions
# Audition can have many medias
# the many gets the foreign key!!! (add to notes)


class User(db.Model):
    """Data model for a user"""

    __tablename__ = 'users'
    # TODO: remove nullables below for testing
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False, unique=True)
    last_name = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        """Display info about user"""

        return f'<User user_id={self.user_id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}>'

########################################################################


class Job(db.Model):
    """Data model for a job"""

    __tablename__ = 'jobs'

    job_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_title = db.Column(db.String(20), nullable=False)
    company = db.Column(db.String(20), nullable=False, unique=True)
    casting_office = db.Column(db.String(20), nullable=True, unique=True)
    agency = db.Column(db.String(20), nullable=True, unique=True)

    def __repr__(self):
        """Display info about user"""

        return f'<Job job_id={self.job_id}, audition_id={self.audition_id}, project_title={self.project_title}, company={self.company}, casting_office={self. casting_office}, agency={self.agency}>'


########################################################################

class Audition(db.Model):
    """Data model for an audition"""

    __tablename__ = 'auditions'

    audition_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.job_id'))
    industry = db.Column(db.String(20), nullable=False, unique=True)
    callback = db.Column(db.Boolean, unique=False, default=False)
    date = db.Column(db.DateTime)
    time = db.Column(db.DateTime)
    role = db.Column(db.String(20), nullable=False,)
    location = db.Column(db.String(20), nullable=True, unique=True)
    notes = db.Column(db.String, nullable=True, unique=True)

    """establishing relationships"""
    user = db.relationship('User', backref='auditions')
    job = db.relationship('Job', backref='auditions')
    media = db.relationship('Media', backref='auditions')

    def __repr__(self):
        """Display info about audition"""

        return f'<Audition audition_id={self.audition_id}, user_id={self.user_id}, job_id={self.job_id}, industry={self.industry}, callback={self.callback}, role={self.role}, location={self.location}, notes={self.notes}>'


########################################################################


class Media(db.Model):
    """Data model for media"""

    __tablename__ = 'media'

    media_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    audition_id = db.Column(db.Integer, db.ForeignKey('auditions.audition_id'))
    title = db.Column(db.String, nullable=False, unique=True)
    link = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        """Display info about media"""

        return f'<Media media_id={self.media_id}, audition_id={self.audition_id}, title={self.title}, link={self.link}>'

########################################################################


def connect_to_db(flask_app, db_uri='postgresql:///followspot', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    db.create_all()
    print('Connected to db!')
