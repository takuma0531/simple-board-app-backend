import os
import pymysql


# save the implemented file to basedir
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  # set up the secret key using environment variable
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-password'
  # set up where the sqlite database file is located
  SQLALCHEMY_DATABASE_URI = os.environ.get('CLEARDB_DATABASE_URL')
  
  # don't let Flask-SQLAlchemy trackk modifications of objects and emit signals
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  