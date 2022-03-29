from decouple import config

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()

def db_connect():
        host = config('DB_HOST')
        port = config('DB_PORT')
        driver = config('DB_CONNECTION')
        username = config('DB_USERNAME')
        password = config('DB_PASSWORD')
        db_name = config('DB_DATABASE')

        connection = f'{driver}://{username}:{password}@{host}:{port}/{db_name}'
        # f'postgresql://postgres:postgres@localhost:5432/db_fluxo_mineracao'
        engine = create_engine(connection, client_encoding='utf8')
        engine.connect()

        return engine
