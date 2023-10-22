## in the init file ? create function that starts the app
from flask import Flask,render_template
from app.config import  project_config as App_Config
from app.models import db
# from app.students.views import  sayhello
from app.students import  student_blueprint


def create_app(config_name='dev'):
    app = Flask(__name__)
    Current_App_Config = App_Config[config_name]
    app.config["SQLALCHEMY_DATABASE_URI"]= Current_App_Config.SQLALCHEMY_DATABASE_URI
    app.config.from_object(Current_App_Config)
    db.init_app(app)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/page_not_found.html')
    #####
    # app.add_url_rule('/hello', view_func=sayhello)
    app.register_blueprint(student_blueprint)


    return app
