#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, jsonify
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

from database.models import Organization, Profile
from .auth.auth import AuthError, requires_auth

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

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()