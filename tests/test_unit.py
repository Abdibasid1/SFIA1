import unittest
import pymysql
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Boxer, Club

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True
        )
        return app

    def setUp(self):
        db.create_all()
        test_club = Club(clubname = "Test the clubname", clublocation= "test the club location", email= "test the club email", clubmanager ="Test the manager")
        db.session.add(test_club)
        db.session.commit()

    def setUp2(self):
        test_boxer = Boxer(firstname = "Test the firstname", lastname= "test the lastname", email= "test the boxer email", weightclass="Test the weightclass", club=1)
        db.session.add(test_boxer)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_addboxer_get(self):
        response = self.client.get(url_for('addboxer'),follow_redirects=True)
        self.assertEqual(response.status_code, 200)
   
    def test_club_get(self):
        response = self.client.get(url_for('club'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_update_get(self):
        response = self.client.get(url_for('update', boxer_id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', boxer_id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_deleteclub_get(self):
        response = self.client.get(url_for('deleteclub', club_id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):
    def test_read_ClubBoxer(self):
        response = self.client.get(url_for("home"))
        self.assertNotIn(b"Test the flask app", response.data)

class TestCreate(TestBase):
    def test_club(self):
        response = self.client.post(
            url_for("club"),
            data=dict(clubname = "Test the clubname", clublocation= "test the club location", email= "test the club email", clubmanager ="Test the manager"),
            follow_redirects=True
        )
        self.assertNotIn(b"Create a new boxer", response.data)
    
    
    def test_addboxer(self):
        response = self.client.post(
            url_for("addboxer"),
            data=dict(firstname = "Test the firstname", lastname= "test the lastname", email= "test the boxer email", weightclass="Test the weighclass", club=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Create a new boxer", response.data)

class TestUpdate(TestBase):
    def test_update_boxer(self):
        response = self.client.post(
            url_for("update", boxer_id=1),
            data=dict(firstname = "Test the firstname", lastname= "test the lastname", email= "test the boxer email", weightclass="Test the weighclass"),
            follow_redirects=True
        )
        self.assertIn(b"not found", response.data)

class TestDelete(TestBase):
    def test_delete_boxerclub(self):
        response = self.client.get(
            url_for("delete", boxer_id=1),
            follow_redirects=True
        )
        self.assertIn(b"not found", response.data)


    def test_delete_club(self):
        response = self.client.get(
            url_for("deleteclub", club_id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"not found", response.data)