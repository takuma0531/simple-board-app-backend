import os
import pymysql


# save the implemented file to basedir
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  # set up the secret key using environment variable
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-password'
  # set up where the sqlite database file is located
  SQLALCHEMY_DATABASE_URI = os.environ.get('CLEARDB_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'posts.db')

  # don't let Flask-SQLAlchemy track modifications of objects and emit signals
  SQLALCHEMY_TRACK_MODIFICATIONS = False