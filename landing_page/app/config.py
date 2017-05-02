#from landing_page import env
# from env import *

FLASK_CONFIG = 'development'
THE_SECRET_KEY = 'd0fbb48c2b61cace96be32a87feea242'
DB_USER = 'b645e0a2b53a96'
DB_PASS = '70e0b973'
DB_NAME = 'heroku_6fda0eae223da40'


# Common configuration
class Config(object):
    """
    # Put any configurations here that are common across all environments
    """

# Development configurations
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SECRET_KEY = THE_SECRET_KEY
    SQLALCHEMY_DATABASE_URI = "mysql://b645e0a2b53a96:70e0b973@us-cdbr-iron-east-03.cleardb.net/heroku_6fda0eae223da40"

    """
    Added the following to suppress warnings in the terminal.
    Not sure of the implications, however, it was saying that it was
    adding significant overhead. So I turned it off.
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Production configurations
class ProductionConfig(Config):
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
