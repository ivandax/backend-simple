import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app, db
from models import Project, Task

class SimpleTaskTestcase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.database_name = "simpletask_dev_test"
        self.database_path = "postgresql://{}/{}".format('postgres@localhost:5432', self.database_name)
        self.app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql://{}/{}".format('postgres@localhost:5432', self.database_name)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.create_all()

        self.projectPayload =  {"name": "TestProject", "status": "active"}
        self.taskPayload =  {"title": "TestTask", "description": "My description", "project_id": 1}
        self.projectPatchPayload =  {"status": "inactive"}
        self.taskPatchPayload =  {"description": "somedesc345"}
        self.validManagerToken = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilc3QkVMUUZIVHE1ODdseS1LemxIXyJ9.eyJpc3MiOiJodHRwczovL2Rldi1pZXRvdmgzZi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjJhZGEyMDdmMzNmNmQ5NzQ2MDZmMjkyIiwiYXVkIjoic2ltcGxldGFzayIsImlhdCI6MTY1NTYyMjU0NiwiZXhwIjoxNjU1Njk0NTQ2LCJhenAiOiIwZk1FSkl0RDZRSFhVblcxeU93eVpYUjcyRXdPM0ZUaSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnRhc2tzIiwiZ2V0OnByb2plY3RzIiwiZ2V0OnRhc2tzIiwicG9zdDpwcm9qZWN0cyIsInBvc3Q6dGFza3MiLCJ1cGRhdGU6cHJvamVjdHMiLCJ1cGRhdGU6dGFza3MiXX0.fUmF1EHHLgY07yGhpWRACzU-ptevD3mKbBUTHZzQ6AczYbX_a6eQL_0M7WJpDZwniUq33JNO2KIBAU8NNhNYjtDyi2iD9t0SvldjC9SvF0L20R0XfmFkJLJ3zzFC-TI1pdXAVfS77pdsBG77cv3k0coresLGA7rEbvneOOhomCHojIJPSdDj2KGP7_SbXVCeSkVcj-Qp6kuLIIVDOTdG3qmBd7DKn418RScrDAzNFQFcLGkHxA8O02NDnBvDMUU-1OdN7O1k86_FJd7gtUXCTYK4J9fT4x1uez9E0Pg8HlcuWrtKOT6e_7tf8OAa-QmZv2SlpPsfwz3pkujjo8w5Kw"
        self.validUserToken = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilc3QkVMUUZIVHE1ODdseS1LemxIXyJ9.eyJpc3MiOiJodHRwczovL2Rldi1pZXRvdmgzZi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjJhZDllY2I0ZGZjNGYxYjk1ZTE0NTRhIiwiYXVkIjoic2ltcGxldGFzayIsImlhdCI6MTY1NTYyMzEyMywiZXhwIjoxNjU1Njk1MTIzLCJhenAiOiIwZk1FSkl0RDZRSFhVblcxeU93eVpYUjcyRXdPM0ZUaSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OnByb2plY3RzIiwiZ2V0OnRhc2tzIl19.Wf9L2x-WlVC4THlF1SpN4g4P3WUPA81aLhYt4p5fPElQkLT_Mvkaou96S6FEAh4jzaJu1ySiymW07YTd36jS8hznGVV9QSfneVIM5OCZ-DfXzCE6rja8ffBUrGEAmR33uH2hplAKWDpdQneHSbnEvtnTAl-JNjsDpllQ8Pg9pJ0mruRYlDWxTWPmwZLRZoOdxHP43rA-qGLlLxfo6SpVlTnvXg0wGmPlU_QjCx4i1qC04DV4dNtHH990Ub2JHCxoejWYT3TtXcQzlHl5dbSlFO6noPoI1y0uZgseuQQsd52kCOB-0g0EsoPLizRBoOlBK_ReOBkBVuBHUSmBs6CILg"


    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_a_post_project_success(self):
        res = self.client().post("/projects", json=self.projectPayload, headers={"Authorization": self.validManagerToken})
        self.assertEqual(res.status_code, 200)

    def test_post_project_failure(self):
        res = self.client().post("/projects", json=self.projectPayload)
        self.assertEqual(res.status_code, 401)

    def test_post_project_failure_user(self):
        res = self.client().post("/projects", json=self.projectPayload, headers={"Authorization": self.validUserToken})
        self.assertEqual(res.status_code, 403)

    def test_get_projects_fail(self):
        res = self.client().get("/projects")
        self.assertEqual(res.status_code, 401)

    def test_get_projects_success(self):
        res = self.client().get("/projects", headers={"Authorization": self.validManagerToken})
        self.assertEqual(res.status_code, 200)

    def test_b_post_task_success(self):
        existing_projects = self.client().get("/projects", headers={"Authorization": self.validManagerToken})
        projects = json.loads(existing_projects.data)
        project_id = projects["items"][0]["id"]
        payload = {"title": "TestTask", "description": "My description", "project_id": project_id}
        res = self.client().post("/tasks", json=payload, headers={"Authorization": self.validManagerToken})
        self.assertEqual(res.status_code, 200)

    def test_post_task_failure(self):
        res = self.client().post("/tasks", json=self.taskPayload)
        self.assertEqual(res.status_code, 401)

    def test_post_task_failure_user(self):
        res = self.client().post("/tasks", json=self.taskPayload, headers={"Authorization": self.validUserToken})
        self.assertEqual(res.status_code, 403)

    def test_get_tasks_fail(self):
        res = self.client().get("/tasks")
        self.assertEqual(res.status_code, 401)

    def test_get_tasks_success(self):
        res = self.client().get("/tasks", headers={"Authorization": self.validManagerToken})
        self.assertEqual(res.status_code, 200)

    def test_y_patch_project_success(self):
        existing_projects = self.client().get("/projects", headers={"Authorization": self.validManagerToken})
        projects = json.loads(existing_projects.data)
        project_id = projects["items"][0]["id"]
        res = self.client().patch("/projects/" + str(project_id), json=self.projectPatchPayload, headers={"Authorization": self.validManagerToken})
        self.assertEqual(res.status_code, 200)

    def test_patch_project_failure(self):
        res = self.client().patch("/projects/1", json=self.projectPatchPayload)
        self.assertEqual(res.status_code, 401)

    def test_y_patch_task_success(self):
        existingTasks = self.client().get("/tasks", headers={"Authorization": self.validManagerToken})
        tasks = json.loads(existingTasks.data)
        task_id = tasks["items"][0]["id"]
        res = self.client().patch("/tasks/" + str(task_id), json=self.taskPatchPayload, headers={"Authorization": self.validManagerToken})
        self.assertEqual(res.status_code, 200)

    def test_patch_task_failure(self):
        res = self.client().patch("/tasks/1", json=self.taskPatchPayload)
        self.assertEqual(res.status_code, 401)

    def test_z_delete_task_success(self):
        existingTasks = self.client().get("/tasks", headers={"Authorization": self.validManagerToken})
        tasks = json.loads(existingTasks.data)
        task_id = tasks["items"][0]["id"]
        res = self.client().delete("/tasks/" + str(task_id), headers={"Authorization": self.validManagerToken})
        self.assertEqual(res.status_code, 200)

    def test_delete_task_failure(self):
        res = self.client().delete("/tasks/1")
        self.assertEqual(res.status_code, 401)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()