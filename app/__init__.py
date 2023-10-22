## in the init file ? create function that starts the app
from flask import Flask
from app.config import  project_config as App_Config
from app.models import db

def create_app(config_name='dev'):
    app = Flask(__name__)
    Current_App_Config = App_Config[config_name]
    app.config["SQLALCHEMY_DATABASE_URI"]= Current_App_Config.SQLALCHEMY_DATABASE_URI
    app.config.from_object(Current_App_Config)
    db.init_app(app)
    return app
