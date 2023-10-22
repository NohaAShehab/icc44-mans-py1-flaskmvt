## in the init file ? create function that starts the app
from flask import Flask


def create_app():
    app = Flask(__name__)

    return app
