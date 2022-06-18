
# Simple Task

This is a task manager app that allows an authenticated user to:

 - Create projects
 - Create tasks by project

Allows businesses to organize, track and prioritize work.

# Starting in development mode:

Run:

`export FLASK_APP=app.py`
`export FLASK_ENV=development`
`flask run`

# Getting Auth0 Credentials for test

There is a frontend that can be run locally to obtain a token from the Auth0 App. Another option is to user your browser to go to:

`https://dev-ietovh3f.us.auth0.com/authorize?audience=simpletask&response_type=token&client_id=0fMEJItD6QHXUnW1yOwyZXR72EwO3FTi&redirect_uri=http://localhost:3000`

This will allow you to log in and get a token.