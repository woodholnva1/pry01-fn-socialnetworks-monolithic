import logging

from flask import render_template, current_app

from repository.RepositoryTable import RepositoryTable

logger = logging.getLogger(__name__)
class ServicesMain:


    def __init__(self):
        self.repositoryTable = RepositoryTable()

    def index(self):
        try:
            lista_registros = self.repositoryTable.GetAllRegister()
            logger.info(f"El tamaño de los Registros es: {len(lista_registros)}")

            return render_template("index.html")
        except Exception as e:
            logger.exception(e.args[0])
            return "ERROR"