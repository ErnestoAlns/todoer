import os
from flask import Flask
from .routes.main import todo

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

def create_app():
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'templates'))
    static_dir = os.path.join(PROJECT_ROOT, 'static')

    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.register_blueprint(todo)
    return app

