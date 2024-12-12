import logging

from flask import render_template, current_app

logger = logging.getLogger(__name__)
class ServicesMain:

    def index(self):
        try:
            logger.error("Entro en la Pagina Comercial!")
            return render_template("index.html")
        except Exception as e:
            logger.exception(e.args[0])
            return "ERROR"