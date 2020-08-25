from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager
from flask_marshmallow import Marshmallow

import os

# local
from config import Configurations

app = Flask(
    __name__,
    template_folder=os.path.abspath('templates'),
    static_folder=os.path.abspath('static'),
)
app.config.from_object(Configurations)

# Initial the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager(app)

ma = Marshmallow(app)

# Blueprints
from Tiles.blueptint import tiles
from Users.blueprint import app_user

# Register models
from Tiles.models import Element, TileStyles, Tile, TileContentFile, TileContentImage, TileContentLink, TileContentVideo

# Registration blueprints
app.register_blueprint(tiles, url_prefix='/tiles')
app.register_blueprint(app_user, url_prefix='/user')
