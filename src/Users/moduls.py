from datetime import datetime

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)

    date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<id: {self.id}; username: {self.username}; email: {self.email}'


class GlobalRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return f'<id: {self.id}; name: {self.name}>'
