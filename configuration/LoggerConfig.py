import logging
import os
from flask.logging import default_handler


# Function to Config Logs
def configLogs():
    # Configurar el logger de errores
    error_log_handler = logging.FileHandler(os.path.join("./logs", "error.log"))
    error_log_handler.setLevel(logging.ERROR)
    error_log_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    error_log_handler.setFormatter(error_log_formatter)

    root = logging.getLogger()
    root.addHandler(default_handler)
    root.addHandler(error_log_handler)
