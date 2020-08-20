import os
from datetime import timedelta


class Configurations:
    DEBUG = True
    SECRET_KEY = 'some secret string'

    template_folder = os.path.abspath('templates')
    static_folder = os.path.abspath('static')

    # database
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234@localhost/Tiles'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Session
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
