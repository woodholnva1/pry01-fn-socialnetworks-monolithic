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


            # Diccionario de Data
            dict_data = {
                "years":["Entre 18-25 años","Entre 26-33 años","Entre 34-40 años","Mas de 40 Años"],
                "sexos":self.repositoryTable.GetAllSexo(),
                "redes":self.repositoryTable.GetAllRedesActive(),
                "horas_redes":self.repositoryTable.GetAllHrsActive()
            }

            return render_template("index.html",data=dict_data)
        except Exception as e:
            logger.exception(e.args[0])
            return "ERROR"