from datetime import datetime as dt
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from api import db


class Movie(db.Model):
    show_id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    director = db.Column(db.String(255), nullable=False)
    cast = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(150), nullable=False)
    #date_added = db.Column(db.DateTime, nullable=True)
    release_year = db.Column(db.Integer(), nullable=False)
    rating = db.Column(db.String(150), nullable=True)
    duration = db.Column(db.String(150), nullable=True)
    listed_in = db.Column(db.String(150), nullable=True)
    description = db.Column(db.Text(150), nullable=True)
    
    def __repr__(self):
        return f"Title: {self.title}, Country: {self.country}, Release_year: {self.release_year}"
    
