from sqlalchemy import func
from model import User, Project, db
from server import app


def test_user():
    """Creates test user in test database"""

    test_user = User(first_name = 'Jennifer', last_name = 'Testman', email = 'testing@testing.com', password = 'jenny', phone="+16507734567")
    db.session.add(test_user)
    db.session.commit()


def test_project():
    """Creates test project in test database"""

    test_project = Image(user_id=1, project_title = "Beetlejuice", industry = "Theatre", company = "Broadway", casting_office="Telsey", agency="Stewart Talent")
    db.session.add(test_project)
    db.session.commit()