import logging
from typing import List

from configuration.ConfigDatabase import ConfigDatabase
from models.entity.Models import RegistroForm, Sexo, RedesSociale, HoraRede

logger = logging.getLogger(__name__)
class RepositoryTable:

    def __init__(self):
        self.db = ConfigDatabase()

    def GetAllRegister(self) -> List[RegistroForm] | None :
        try:
            with self.db as sessionSqlite:
                registros_all = sessionSqlite.query(RegistroForm).all()
            return registros_all
        except Exception as e:
            logger.exception(f"Error metodo BD GetAllRegister() {e.args[0]}")
            return None

    def GetAllSexo(self) -> List[Sexo] | None :
        try:
            with self.db as sessionSqlite:
                registros_all_sexo = sessionSqlite.query(Sexo).all()
            return registros_all_sexo
        except Exception as e:
            logger.exception(f"Error metodo BD GetAllSexo() {e.args[0]}")
            return None

    def GetAllRedesActive(self) -> List[RedesSociale] | None :
        try:
            with self.db as sessionSqlite:
                registros_all_redes = sessionSqlite.query(RedesSociale).filter(RedesSociale.status == 1).all()
            return registros_all_redes
        except Exception as e:
            logger.exception(f"Error metodo BD GetAllRedesActive() {e.args[0]}")
            return None

    def GetAllHrsActive(self) -> List[HoraRede] | None :
        try:
            with self.db as sessionSqlite:
                registros_all_hrs = sessionSqlite.query(HoraRede).filter(HoraRede.status == 1).all()
            return registros_all_hrs
        except Exception as e:
            logger.exception(f"Error metodo BD GetAllHrsActive() {e.args[0]}")
            return None
