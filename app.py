#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
# Imports config vars from config file
app.config.from_object('config')
db = SQLAlchemy(app)
# Add migration config
migrate = Migrate(app, db)

from database.models import Project, Task
from auth.auth import AuthError, requires_auth


#----------------------------------------------------------------------------#
# Endpoints
#----------------------------------------------------------------------------#

@app.route("/", methods=["GET"])
def test():       
    return jsonify({
            "success": True,
            "action": "This is running!"
        }
    )

@app.route("/projects", methods=["GET"])
@requires_auth("get:projects")
def get_projects(jwt):
    projects = Project.query.order_by(Project.id).all()
    formatted = [project.format() for project in projects]
    return jsonify({
        "success": True,
        "items": formatted,
         })



@app.route("/projects", methods=["POST"])
@requires_auth("post:projects")
def add_project(jwt):
    body = request.get_json()
    userId = jwt["sub"]
    if body:
        name = body.get("name", None)
        status = body.get("status", None)
        if name != None and status != None:
            try:
                project = Project(name=name, status=status, created_by=userId)
                project.insert()
                return jsonify({
                    "success": True,
                })
            except:
                print(sys.exc_info())
                abort(400)
        else:
            abort(422)
    else:
        abort(422)

@app.route("/projects/<int:project_id>", methods=["PATCH"])
@requires_auth("update:projects")
def update_project(jwt, project_id):
    project = Project.query.filter(Project.id == project_id).one_or_none()

    if project is None:
        abort(404)

    body = request.get_json()
    name = body.get("name", None)
    status = body.get("status", None)

    if name is not None:
        project.name = name
    if status is not None:
        project.status = status

    try:
        project.update()
        return jsonify({
            "success": True,
        })
    except:
        print(sys.exc_info())
        abort(400)

@app.route("/tasks", methods=["POST"])
@requires_auth("post:tasks")
def add_task(jwt):
    body = request.get_json()
    userId = jwt["sub"]
    if body:
        title = body.get("title", None)
        description = body.get("description", None)
        project_id = body.get("project_id", None)

        if project_id is None:
            abort(400)

        if title != None and description != None:
            try:
                project = Project.query.get(project_id)
                if project is None:
                     abort(404)
                task = Task(title=title, description=description, created_by=userId, project_id=project_id)
                task.insert()
                return jsonify({
                    "success": True,
                })
            except:
                print(sys.exc_info())
                abort(400)
        else:
            abort(422)
    else:
        abort(422)

#----------------------------------------------------------------------------#
# Error handlers
#----------------------------------------------------------------------------#

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "code": 422,
        "message": "resource not processable"
    }), 422

@app.errorhandler(401)
def access_denied(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "access denied"
    }), 401

@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        "success": False,
        "error": 403,
        "message": "forbidden"
    }), 403

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400



@app.errorhandler(AuthError)
def process_AuthError(error):
    response = jsonify(error.error)
    response.status_code = error.status_code

    return response

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()