import os
import pymysql


# save the implemented file to basedir
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  # set up the secret key using environment variable
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-password'
  # set up where the sqlite database file is located
  SQLALCHEMY_DATABASE_URI = os.environ.get('CLEARDB_DATABASE_URL') or  'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format('mysql+pymysql://b83f86ae979173:d7298307@us-cdbr-iron-east-01.cleardb.net/heroku_bd2f9e40800166b?reconnect=true')
  
  # don't let Flask-SQLAlchemy trackk modifications of objects and emit signals
  SQLALCHEMY_TRACK_MODIFICATIONS = False