#from landing_page import env
from env import *

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
    SQLALCHEMY_DATABASE_URI = "mysql://" + DB_USER + ":" + DB_PASS + "@localhost/" + DB_NAME

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
