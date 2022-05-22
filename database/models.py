import os
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy.sql.schema import PrimaryKeyConstraint
import datetime

from app import db

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Organization(db.Model):
    __tablename__ = 'organizations'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String)
    user_quota = Column(Integer)

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
    name = Column(String)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, default=datetime.datetime.utcnow)
    organization_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)

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
            "name": self.name,
            "created": self.created,
            "updated": self.updated,
            "organization_id": self.organization_id,
        }