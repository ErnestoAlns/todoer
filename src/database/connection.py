import mysql.connector
from flask import g
from .config import db_config

def get_db_connection():
    if 'db_connection' not in g:
        config = db_config()
        try:
            g.db_connection = mysql.connector.connect(**config)

        except mysql.connector.Error as err:
            raise RuntimeError(f'Data base connection faild: { err }',)

    return g.db_connection


