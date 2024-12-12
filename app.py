
from flask import Flask
from configuration.LoggerConfig import configLogs
from views.MainViews import main_bp
app = Flask(__name__)

# Registrar Vistas del Controller Views
app.register_blueprint(main_bp)
configLogs()

if __name__ == '__main__':
    app.run(debug=True)

