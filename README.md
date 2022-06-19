# Final Project for Udacity Fullstack Course

## Simple Task

This is a task manager app that allows an authenticated user to:

- Create projects
- Create tasks by project

This project could be extended to add more functionalities to help businesses track their projects and tasks.

## Existing Auth0 users (RBAC controls)

There are 2 roles in this app:

- A manager that can Read, Create, Update and Delete all tasks and projects
- A user that can only Read tasks and projects

Two accounts exist already in Auth0 to support this:

- simpletaskmanager@gmail.com for Manager Role
- simpletaskuser@gmail.com for User role

## Getting Auth0 Credentials for test

Use your browser to go to:

`https://dev-ietovh3f.us.auth0.com/authorize?audience=simpletask&response_type=token&client_id=0fMEJItD6QHXUnW1yOwyZXR72EwO3FTi&redirect_uri=http://localhost:3000`

This will allow you to log in and get a token.

## Testing Endpoints in Postman

All endpoints need a JWT to work. All of them are protected so you need to get a token with the link above and one of the 2 accounts.

After that, you can download the Postman collection in file `TaskManager.postman_collection2`

Here you can replace the tokens in the Authorization section to test them.

Currently, the token provided in the Postman collection is valid and the time is extended. It's for the role of the Manager, so all endpoints should work.

There are options for local and Heroku.

## Heroku link:

`https://backend-simple.herokuapp.com/`

## Project dependencies:

alembic==1.6.5
autopep8==1.6.0
Babel==2.9.0
click==8.1.2
colorama==0.4.4
Flask==1.1.2
Flask-Script==2.0.6
Flask-Migrate==2.7.0
Flask-Moment==0.11.0
Flask-SQLAlchemy==2.5.1
greenlet==1.1.2
itsdangerous==2.0.1
Mako==1.2.0
MarkupSafe==2.1.1
psycopg2==2.9.3
pycodestyle==2.8.0
python-dateutil==2.6.0
pytz==2022.1
six==1.16.0
SQLAlchemy==1.4.35
toml==0.10.2
Werkzeug==2.0.3
WTForms==3.0.1
python-jose==3.2.0
pycryptodome==3.14.1
wrapt==1.11.1
gunicorn==20.1.0
Jinja2==3.0.1

## Hosting

The current app is hosted in Heroku, linked to the github repo (branch main):

`https://github.com/ivandax/backend-simple`

When you make updates to the app. You have to push changes to your repo, but also to Heroku:

`git push heroku main`

## Starting in development mode:

Install the dependencies.

`source Scripts/activate` To activate the local environment and use dependencies only for this project
Then you can:
`pip install -r requirements.txt`

It uses Postgres locally.

You need postgres running locally and to create a DB called `simpletask_dev`

Then you can do the migrations:

```
flask db init
flask db migrate
flask db upgrade
```

Then to start in dev mode:

`export FLASK_APP=app.py`
`export FLASK_ENV=development`
`flask run`

## API Arquitecture (Endpoints):

All existing endpoints are protected and require user authentication. 

There are 2 roles, a Manager that can do all CRUD operations. 
And a User than can only do Read operations.

There are 2 tables in the DB, projects and tasks.
A project can have many tasks.

### Endpoints

`POST /projects`

Creates a project. Requires to send a payload of form:

```
{
    "name": "My Project",
    "status": "active"
}
```

`POST /tasks`

Creates a task. Requires to send a payload of form:

```
{
    "title": "My new task",
    "description": "I love udacity",
    "project_id": 1
}
```

`PATCH /projects/:id`

Updates a project. Requires to send a payload of form:

```
{
    "name": "Pizza Project",
    "status": "inactive"
}
```

`PATCH /tasks/:id`

Updates a task. Requires to send a payload of form:

```
{
    "title": "Machine task",
    "description": "This is my description"
}
```

`DELETE /tasks/:id`

Deletes a given task.

`GET /projects`

Reads existing projects. Will return a response of form:

```
{
    "items": [
        {
            "created": "Sat, 18 Jun 2022 14:44:28 GMT",
            "created_by": "auth0|62ada207f33f6d974606f292",
            "id": 1,
            "name": "The apricot mill!!",
            "status": "active",
            "updated": "Sat, 18 Jun 2022 14:44:28 GMT"
        },
        {
            "created": "Sat, 18 Jun 2022 14:45:57 GMT",
            "created_by": "auth0|62ada207f33f6d974606f292",
            "id": 2,
            "name": "War Machine!",
            "status": "active",
            "updated": "Sat, 18 Jun 2022 14:45:57 GMT"
        },
    ],
    "success": true
}
```

`GET /tasks`

Reads existing tasks. Will return a response of form:

```
{
    "items": [
        {
            "created_by": "auth0|62ada207f33f6d974606f292",
            "description": "The after make like lik 22",
            "id": 1,
            "project_id": 1,
            "title": "Try some stuffc 2244",
            "updated": "Sat, 18 Jun 2022 14:46:24 GMT"
        },
        {
            "created_by": "auth0|62ada207f33f6d974606f292",
            "description": "You have to build them!",
            "id": 2,
            "project_id": 4,
            "title": "Build some stone structures",
            "updated": "Sun, 19 Jun 2022 07:12:31 GMT"
        },
    ],
    "success": true
}
```





