import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app, db
from database.models import Project, Task

class TriviaTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.database_name = "simpletask_dev_test"
        self.database_path = "postgresql://{}/{}".format('postgres@localhost:5432', self.database_name)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.create_all()

        self.validToken = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilc3QkVMUUZIVHE1ODdseS1LemxIXyJ9.eyJpc3MiOiJodHRwczovL2Rldi1pZXRvdmgzZi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjJhZDllY2I0ZGZjNGYxYjk1ZTE0NTRhIiwiYXVkIjoic2ltcGxldGFzayIsImlhdCI6MTY1NTU0NTcxOSwiZXhwIjoxNjU1NTUyOTE5LCJhenAiOiIwZk1FSkl0RDZRSFhVblcxeU93eVpYUjcyRXdPM0ZUaSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OnByb2plY3RzIiwiZ2V0OnRhc2tzIl19.TJznoLQDNSXWWa8eso_zjoTUqpmpMATzo-w1Ox9EfHnHL2Jv0wMKiY0r_wdhyK-GePKsVxXU2FcbVYitGpJntEv4Q3bq6PARm-e74XP22fXvrb-KXocZcZy6xrFujymVx1EFkPwjQyrB1XHnxGO8780Hsk2nTAgQekvIEFZg88aHgKxjQ8qZM8EGgUygolR4Qat8IPJJgzKIHlTo4ewENTMElp4X1malcIphTWyzcgZrAKlPEOe5eqAS7sPSmwkv_gQC5pJOk6Y1F5_G2LvFwrkr4zZf8KAJ4_T8BzQlUjfn3lEhOI-7D_QrF1j2TGQtZKSoRL51WkFwhHgwWyTj8g"
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_projects_fail(self):
        res = self.client().get("/projects")
        data =json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    def test_get_projects_success(self):
        res = self.client().get("/projects", headers={"Authorization": self.validToken})
        data =json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["items"])

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()