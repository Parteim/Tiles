from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from app import db, app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))

    date = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f'<id: {self.id}; username: {self.username}; email: {self.email}'

    def check_password(self, password):
        return check_password_hash(self.password, password)


class GlobalRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return f'<id: {self.id}; name: {self.name}>'
