# third-party imports
from flask import Flask
from flask_session import Session

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# local imports
from config import app_config
# from env import *

FLASK_CONFIG = 'development'
THE_SECRET_KEY = 'd0fbb48c2b61cace96be32a87feea242'
DB_USER = 'b645e0a2b53a96'
DB_PASS = '70e0b973'
DB_NAME = 'heroku_6fda0eae223da40'

# db variable initialization
db = SQLAlchemy()

# create the actual Flask app and our associated db objects based on a given config_name
def create_app(config_name) :
    # App config
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # DB config
    db.init_app(app)

    # Migration config
    migration = Migrate(app, db)

    # Session config
    app.secret_key = THE_SECRET_KEY
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)

    # Finally return our app object
    return app
