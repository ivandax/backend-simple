import os
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
import json
from sqlalchemy.sql.schema import PrimaryKeyConstraint
import datetime

from app import db

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Project(db.Model):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, nullable=False)
    created_by = Column(String, nullable=False)
    tasks = db.relationship("Task", backref='list', lazy=True, cascade="all, delete-orphan")

    def __init__(self, name, status, created_by ):
        self.name = name
        self.status = status
        self.created_by = created_by
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "created": self.created,
            "updated": self.updated,
            "status": self.status,
            "created_by": self.created_by
        }

class Task(db.Model):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String, unique=True, nullable=False)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(String, nullable=False)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)

    def __init__(self, title, description, created_by ):
        self.title = title
        self.description = description
        self.created_by = created_by
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "updated": self.updated,
            "created_by": self.created_by,
            "project_id": self.project_id
        }


# The Following models are not used in the current version of the app.
class Organization(db.Model):
    __tablename__ = 'organizations'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, nullable=False)
    user_quota = Column(Integer, nullable=False)

    def __init__(self, name,status, user_quota ):
        self.name = name
        self.status = status
        self.user_quota = user_quota
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "created": self.created,
            "updated": self.updated,
            "status": self.status,
            "user_quota": self.user_quota
        }

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, default=datetime.datetime.utcnow)
    organization_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)
    language = Column(String)

    def __init__(self, name, organization_id):
        self.name = name
        self.organization_id = organization_id
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "created": self.created,
            "updated": self.updated,
            "organization_id": self.organization_id,
            "language": self.language,
        }
