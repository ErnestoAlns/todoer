import os
from decouple import config
from flask import Flask, g
from .routes.main import todo

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

def create_app():
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'templates'))
    static_dir = os.path.join(PROJECT_ROOT, 'static')

    SECRET_KEY = config('SECRET_KEY')
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.register_blueprint(todo)

    app.config['SECRET_KEY'] = SECRET_KEY

    @app.teardown_appcontext
    def close_db_connection(exception):
        conn = g.pop('db_connection', None)
        if conn is not None:
            try:
                if exception:
                    conn.rollback() 
                else:
                    conn.commit()
            except Exception as e:
                print(f"Error al intentar cerrar la transacción: {e}")

            finally:
                conn.close()

            pass
    return app

