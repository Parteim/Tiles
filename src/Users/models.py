from datetime import datetime

from idna import unicode
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))

    date = db.Column(db.DateTime, default=datetime.now())

    profile = db.relationship('Profile', uselist=False, back_populates='user')

    tiles = db.relationship('Tile', back_populates='author')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f'<id: {self.id}; username: {self.username}; email: {self.email}>'

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


class GlobalRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return f'<id: {self.id}; name: {self.name}>'


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='profile')

    image = db.Column(db.String(255))

    def __init__(self, user):
        self.user = user

    def __repr__(self):
        return f'<id: {self.id}; user: {self.user}>'