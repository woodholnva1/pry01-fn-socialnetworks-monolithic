import os

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker


class ConfigDatabase:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join('formularios.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    def __init__(self):
        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URI, echo=self.SQLALCHEMY_ECHO)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def __enter__(self):
        return self.SessionLocal()

    def __exit__(self, exc_type, exc_value, traceback):
        self.SessionLocal().close()

    def test_connection(self):
        # Verificar si el archivo de base de datos existe
        db_path = self.SQLALCHEMY_DATABASE_URI.split('///')[-1]
        if not os.path.exists(db_path):
            return False
        try:
            with self.engine.connect() as connection:
                return True
        except OperationalError:
            return False
