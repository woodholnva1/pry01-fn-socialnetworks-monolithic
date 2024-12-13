import logging
from typing import List

from configuration.ConfigDatabase import ConfigDatabase
from models.Models import RegistroForm

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