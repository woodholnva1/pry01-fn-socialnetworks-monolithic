import logging
from sqlalchemy import and_
from typing import List

from configuration.ConfigDatabase import ConfigDatabase
from models.beans.registerSurveyRequest import redes
from models.entity.Models import RegistroForm, Sexo, RedesSociale, HoraRede, RelFormRedesHr

logger = logging.getLogger(__name__)


class RepositoryTable:

    def __init__(self):
        self.db = ConfigDatabase()

    def GetAllRegister(self) -> List[RegistroForm] | None:
        try:
            with self.db as sessionSqlite:
                registros_all = sessionSqlite.query(RegistroForm).all()
            return registros_all
        except Exception as e:
            logger.exception(f"Error metodo BD GetAllRegister() {e.args[0]}")
            return None

    def GetAllSexo(self) -> List[Sexo] | None:
        try:
            with self.db as sessionSqlite:
                registros_all_sexo = sessionSqlite.query(Sexo).all()
            return registros_all_sexo
        except Exception as e:
            logger.exception(f"Error metodo BD GetAllSexo() {e.args[0]}")
            return None

    def GetAllRedesActive(self) -> List[RedesSociale] | None:
        try:
            with self.db as sessionSqlite:
                registros_all_redes = sessionSqlite.query(RedesSociale).filter(RedesSociale.status == 1).all()
            return registros_all_redes
        except Exception as e:
            logger.exception(f"Error metodo BD GetAllRedesActive() {e.args[0]}")
            return None

    def GetAllHrsActive(self) -> List[HoraRede] | None:
        try:
            with self.db as sessionSqlite:
                registros_all_hrs = sessionSqlite.query(HoraRede).filter(HoraRede.status == 1).all()
            return registros_all_hrs
        except Exception as e:
            logger.exception(f"Error metodo BD GetAllHrsActive() {e.args[0]}")
            return None

    def GetRedesActiveById(self, id_red: int) -> RedesSociale | None:
        try:
            with (self.db as sessionSqlite):
                registros_redes = sessionSqlite.query(RedesSociale
                                                      ).filter(and_(RedesSociale.status == 1,
                                                                    RedesSociale.id_red_social == id_red)).all()
            return registros_redes
        except Exception as e:
            logger.exception(f"Error metodo BD GetRedesActiveById() {e.args[0]}")
            return None

    def RegisterSurvey(self, registroForm: RegistroForm, array_redes_objet: List[redes]) -> bool:
        try:
            with (self.db as sessionSqlite):
                sessionSqlite.add(registroForm)
                sessionSqlite.flush()

                # Registrar la relacion de las redes y las Hrs
                for reg in array_redes_objet:
                    currentRelFormRedesHr = RelFormRedesHr()
                    currentRelFormRedesHr.id_form = registroForm.id
                    currentRelFormRedesHr.id_hora = int(reg.value)
                    currentRelFormRedesHr.id_red = int(reg.id_red)
                    sessionSqlite.add(currentRelFormRedesHr)
                sessionSqlite.flush()
                sessionSqlite.commit()
            return True
        except Exception as e:
            logger.exception(f"Error metodo BD RegisterSurvey() {e.args[0]}")
            return False
