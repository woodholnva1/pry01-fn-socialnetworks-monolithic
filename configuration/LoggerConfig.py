import logging
import os
from flask.logging import default_handler


# Function to Config Logs
def configLogs():
    log_dir = "./logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Configurar el logger de errores
    error_log_handler = logging.FileHandler(os.path.join(log_dir, "error.log"))
    error_log_handler.setLevel(logging.ERROR)
    error_log_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    error_log_handler.setFormatter(error_log_formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(console_handler_formatter)

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    root.addHandler(error_log_handler)
    root.addHandler(console_handler)