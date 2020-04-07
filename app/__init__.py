from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# init Flask itself
app = Flask(__name__)
# disable serializing JSON objects in a way that the keys are ordered
app.config['JSON_SORT_KEYS'] = False

app.config.from_object(Config)

# init database
db = SQLAlchemy(app)
# init Marshmallow
ma = Marshmallow(app)
# add a migration engine
migrate = Migrate(app, db)
# set up Cross Origin Resource Sharing
CORS(app, resources={r'/*': {'origins': '*'}})

from app import routes, models