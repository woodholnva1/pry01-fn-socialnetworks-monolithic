from typing import Any, List

import logging
from flask import render_template, jsonify
from pydantic import ValidationError

from models.beans.registerSurveyRequest import RegisterSurveyRequset
from models.entity.Models import RegistroForm, RelFormRedesHr
from models.response.beansResponse import BeanResponse
from repository.RepositoryTable import RepositoryTable

logger = logging.getLogger(__name__)


class ServicesMain:

    def __init__(self):
        self.repositoryTable = RepositoryTable()
        self.beanResponse = BeanResponse()

    def index(self):
        try:

            # Diccionario de Data
            dict_data = {
                "years": ["Entre 18-25 años", "Entre 26-33 años", "Entre 34-40 años", "Mas de 40 Años"],
                "sexos": self.repositoryTable.GetAllSexo(),
                "redes": self.repositoryTable.GetAllRedesActive(),
                "horas_redes": self.repositoryTable.GetAllHrsActive()
            }

            return render_template("index.html", data=dict_data)
        except Exception as e:
            logger.exception(e.args[0])
            return self.beanResponse.notesperated(e.args[0])

    # Logica para Verificar si el Correo esta Disponible
    def verifyMail(self, mail) -> dict:
        try:
            # Si no posee parametro Indicar Error
            if not mail:
                return self.beanResponse.notfound("Debe ingresar un parametro correctamente", "Param not Found", )
            #
            correo_existe = [x for x in self.repositoryTable.GetAllRegister() if
                             x.email.upper().strip() == mail.upper().strip()]

            if len(correo_existe) != 0:
                return self.beanResponse.notesperated("Ya este correo realizo la Encuesta, intenta con Otro!")

            # Seguir con el Flujo!
            return self.beanResponse.success("Correo verificado Correctamenteo!!", "Correo Validado Correctamente!")
        except Exception as e:
            logger.exception(e.args[0])
            return self.beanResponse.notesperated(e.args[0])

    # ----------------------------------------------------------------------------------------
    # Endpoint para Registrar Encuesta
    #
    def registerSurvey(self, json_request: dict) -> dict:
        try:
            # Validacion con Pydantic directa!
            register_survey_request = RegisterSurveyRequset(**json_request)
            registro_form = RegistroForm()
            registro_form.redPreferida = int(register_survey_request.favorite_network)
            registro_form.edad = register_survey_request.years
            registro_form.email = register_survey_request.mail
            registro_form.sexo  = int(register_survey_request.sex)

            if self.repositoryTable.RegisterSurvey(registro_form,register_survey_request.redes_sociales):
                return self.beanResponse.success("Encuesta Enviada Correctamente!!",
                                                 "Encuesta Registrada correctamente!")
            else:
                return self.beanResponse.notesperated("No se pudo Registrar la Encuesta!")

        # Except si el json es Invalido
        except ValidationError as validateJson:
            return self.beanResponse.invalidRequest("Error al enviar el json!")
        except Exception as e:
            logger.exception(e.args[0])
            return self.beanResponse.notesperated(e.args[0])
