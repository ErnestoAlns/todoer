from decouple import config

def db_config():
    return {
            'host': config('DB_HOST'),
            'database': config('DB_NAME'),
            'user': config('DB_USER'),
            'password': config('DB_PASSWORD')

            }
