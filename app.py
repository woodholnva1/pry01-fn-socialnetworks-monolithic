import os
from sqlite3 import OperationalError
from sqlalchemy import create_engine
from flask import Flask

from configuration.ConfigDatabase import ConfigDatabase
from configuration.LoggerConfig import configLogs
from views.MainViews import main_bp

def runApp():
    app = Flask(__name__)

    # Registrar Vistas del Controller Views
    app.register_blueprint(main_bp)

    # Probar la Conexion con la Base de datos
    config_db = ConfigDatabase()
    if not config_db.test_connection():
        app.logger.error(
            "Error connecting to the database. Check server configuration and availability!")
        return None
    configLogs()

    return app

# Inicio to APP
if __name__ == '__main__':
    app = runApp()
    # Configuracion Correcta Inicia la Aplicacion
    if app:
        app.run(debug=True)