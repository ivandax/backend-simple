
# Final Project for Udacity Fullstack Course
# Simple Task

This is a task manager app that allows an authenticated user to:

 - Create projects
 - Create tasks by project

This project could be extended to add more functionalities to help businesses track their projects and tasks.

# Starting in development mode:

Install the dependencies.
It uses Postgres locally.

Run:

`export FLASK_APP=app.py`
`export FLASK_ENV=development`
`flask run`

# Existing Auth0 users

There are 2 roles in this app:

- A manager that can Read, Create, Update and Delete all tasks and projects
- A user that can only Read tasks and projects

Two accounts exist already in Auth0 to support this:

- simpletaskmanager@gmail.com for Manager Role
- simpletaskuser@gmail.com for User role

# Getting Auth0 Credentials for test

There is a frontend that can be run locally to obtain a token from the Auth0 App. Another option is to user your browser to go to:

`https://dev-ietovh3f.us.auth0.com/authorize?audience=simpletask&response_type=token&client_id=0fMEJItD6QHXUnW1yOwyZXR72EwO3FTi&redirect_uri=http://localhost:3000`

This will allow you to log in and get a token.

