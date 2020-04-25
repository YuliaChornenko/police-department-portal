import logging
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from config import Config
from flask_cors import CORS

logging.getLogger().setLevel(logging.DEBUG)
app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager(app)
bootstrap = Bootstrap(app)

CORS(app)
app.debug = True

from app import routes
