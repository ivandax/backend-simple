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

        self.projectPayload =  {"name": "TestProject6699", "status": "active"}
        self.taskPayload =  {"title": "TestTask199", "description": "My description1199", "project_id": 1}
        self.validToken = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilc3QkVMUUZIVHE1ODdseS1LemxIXyJ9.eyJpc3MiOiJodHRwczovL2Rldi1pZXRvdmgzZi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjJhZGEyMDdmMzNmNmQ5NzQ2MDZmMjkyIiwiYXVkIjoic2ltcGxldGFzayIsImlhdCI6MTY1NTU0NjQ4NSwiZXhwIjoxNjU1NTUzNjg1LCJhenAiOiIwZk1FSkl0RDZRSFhVblcxeU93eVpYUjcyRXdPM0ZUaSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnRhc2tzIiwiZ2V0OnByb2plY3RzIiwiZ2V0OnRhc2tzIiwicG9zdDpwcm9qZWN0cyIsInBvc3Q6dGFza3MiLCJ1cGRhdGU6cHJvamVjdHMiLCJ1cGRhdGU6dGFza3MiXX0.iWHQOKiB9sB1haqQaKITHqQ8K62bJk0ZlE1VlSzrgvcRtKuw9nC4xxWkyFPmTWpUrhwcXCypJsntmen_R66b0NqHDLXWz_xEb5sOe6vYOBBrfAS7FKcxJB2Py9K_ME0fmgDzWWZ2TgeAfLXAlIG14UUCL0OMndLNZSf3CVzXwGUs4IPyr3zD9bGgvRGM4efUWIXjMG-1lR3UlXeEanKh8DrRTj6tOf1P8E2nVkwnoJLJtFzaGUoSaJQwIlm0pfDkRO8AShUygXsuy-PJ5pGdLFqmVNxQC62rZa-SV3lrF8RwcBMXgjb4OJ5HGkyPX1M9SQd-FfJDqwO3v27sFDmnNA"
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_post_project_success(self):
        res = self.client().post("/projects", json=self.projectPayload, headers={"Authorization": self.validToken})
        data =json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_post_project_failure(self):
        res = self.client().post("/projects", json=self.projectPayload)
        data =json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    def test_get_projects_fail(self):
        res = self.client().get("/projects")
        data =json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    def test_get_projects_success(self):
        res = self.client().get("/projects", headers={"Authorization": self.validToken})
        data =json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["items"])

    def test_post_task_success(self):
        res = self.client().post("/tasks", json=self.taskPayload, headers={"Authorization": self.validToken})
        data =json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_post_task_failure(self):
        res = self.client().post("/tasks", json=self.taskPayload)
        data =json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    def test_get_tasks_fail(self):
        res = self.client().get("/tasks")
        data =json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    def test_get_tasks_success(self):
        res = self.client().get("/tasks", headers={"Authorization": self.validToken})
        data =json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["items"])

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()