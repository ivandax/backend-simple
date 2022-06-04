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

from database.models import Organization, Profile, Project
from auth.auth import AuthError, requires_auth


#----------------------------------------------------------------------------#
# Endpoints
#----------------------------------------------------------------------------#

@app.route("/test", methods=["GET"])
def test():       
    return jsonify({
            "success": True,
            "action": "test"
        }
    )

@app.route("/projects", methods=["POST"])
@requires_auth("post:projects")
def add_project(jwt):
    body = request.get_json()
    if body:
        name = body.get("name", None)
        status = body.get("status", None)
        created_by = body.get("created_by", None)
        if name != None and status != None and created_by != None:
            try:
                project = Project(name=name, status=status, created_by=created_by)
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

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()