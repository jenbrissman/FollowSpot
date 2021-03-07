from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

###########################USER#############################################

class User(db.Model):
    """Data model for a user"""
    # TODO: remove nullables below for testing

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    phone = db. Column(db.String(20), nullable=False)

    projects = db.relationship('Project', backref='user')

    def __repr__(self):
        """Display info about user"""

        return f'<User user_id={self.user_id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}, password={self.password}, phone={self.phone}>'

############################PROJECT############################################

class Project(db.Model):
    """Data model for a project"""

    __tablename__ = 'projects'

    project_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    industry = db.Column(db.String(20))
    project_title = db.Column(db.String(20))
    company = db.Column(db.String(20))
    casting_office = db.Column(db.String(20))
    agency = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        """Display info about user"""

        return f'<Project project_id={self.project_id}, user_id={self.user_id}, industry={self.industry}, project_title={self.project_title}, company={self.company}, casting_office={self. casting_office}, agency={self.agency}>'


##########################AUDITION##############################################

class Audition(db.Model):
    """Data model for an audition"""

    __tablename__ = 'auditions'

    audition_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))
    callback = db.Column(db.String(5))
    date = db.Column(db.String(20))
    time = db.Column(db.String(20))
    location = db.Column(db.String(20))
    role = db.Column(db.String(20))
    notes = db.Column(db.String, nullable=True)

    """establishing relationships"""
    user = db.relationship('User', backref='auditions')
    project = db.relationship('Project', backref='auditions')
    medias = db.relationship('Media', backref='auditions')

    def __repr__(self):
        """Display info about audition"""

        return f'<Audition audition_id={self.audition_id}, user_id={self.user_id}, project_id={self.project_id}, date={self.date}, time={self.time}, callback={self.callback}, role={self.role}, location={self.location}, notes={self.notes}>'


##########################MEDIA##############################################


class Media(db.Model):
    """Data model for media"""

    __tablename__ = 'media'

    media_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    audition_id = db.Column(db.Integer, db.ForeignKey('auditions.audition_id'))
    media_title = db.Column(db.String)
    link = db.Column(db.String)

    user = db.relationship('User', backref='media')

    def __repr__(self):
        """Display info about media"""

        return f'<Media media_id={self.media_id}, audition_id={self.audition_id}, media_title={self.media_title}, link={self.link}>'

########################################################################


def connect_to_db(flask_app, db_uri='postgresql:///followspot', echo=False):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all()
    print('Connected to db!')
