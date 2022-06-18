import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost:5432/simpletask_dev'
SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
SQLALCHEMY_TRACK_MODIFICATIONS = False