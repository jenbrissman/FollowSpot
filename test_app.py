import os
from flask_sqlalchemy import SQLAlchemy
from server import app
from unittest import TestCase
from flask import session
from model import db, connect_to_db
from test_seed import test_user, test_project
import unittest
import testing.postgresql
from sqlalchemy import create_engine
import psycopg2

import os
import tempfile
# import pytest

class PowTests(TestCase):
    """Tests Pow site"""

    def setUp(self):
        """Code to run before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_home(self):
        """Tests homepage"""

        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'<p class="message"> Not registered?', result.data)


class TestPowLoggedIn(TestCase):
    """Tests if a user is logged in correctly"""

    @classmethod
    def setUp(self):
            """Code to run before every test."""

            self.client = app.test_client()
            self.postgresql = testing.postgresql.Postgresql(name="testdb", port=7654)
            
            engine = create_engine(self.postgresql.url())

            app.config['TESTING'] = True
            # connect_to_db(app, db_uri=testdb)
            connect_to_db(app, db_uri="postgresql:///testdb")
            db.create_all()
            test_user()
            test_project()

            with self.client as c:
                        with c.session_transaction() as session:
                            session['user_id'] = 1

    def test_feed(self):
            """Tests feed page that displays audition information"""
            with self.client as c:
                result = c.get('/feed')
                self.assertEqual(result.status_code, 200)
                self.assertIn(b'id="audition-info"', result.data)
    
    def test_input(self):
            """Tests input form page"""
            with self.client as c:
                result = c.get('/input')
                self.assertEqual(result.status_code, 200)
                self.assertIn(b'id="audition-form"', result.data)
                          

    def test_logout(self):
        """Tests if user gets logged out of session"""
        with self.client as c:
            with c.session_transaction() as session:
                session["user_id"]=1
            result = c.get('/logout', follow_redirects=True)
                
            self.assertNotIn(b'user_id', session)

    @classmethod
    def tearDown(self):
            """Code to run after every test"""
            
            db.session.remove()
            db.drop_all()
            db.engine.dispose()

            self.postgresql.stop()


if __name__ == '__main__': 
    import unittest
    unittest.main()