import os


class Configurations:
    DEBUG = True
    SECRET_KEY = 'some secret string'

    template_folder = os.path.abspath('templates')
    static_folder = os.path.abspath('static')

    # database
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234@localhost/Tiles'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
