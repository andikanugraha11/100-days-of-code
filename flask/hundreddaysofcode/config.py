import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    POSTGRES = {
        'user'      : 'postgres',
        'password'  : 'mysecretpassword',
        'db'        : 'hundreddaysofcode_flask',
        'host'      : 'localhost',
        'port'      : '5432',
    }
    SQLALCHEMY_DATABASE_URI= 'postgresql://%(user)s:\%(password)s@%(host)s:%(port)s/%(db)s' % POSTGRES

class TestingConfig(Config):
    TESTING = True