from typing import List
from pydantic import BaseModel

class redes(BaseModel):
    id_red:int = None
    value:int  = None

class RegisterSurveyRequset(BaseModel):
    mail:str
    years:str
    sex:int
    favorite_network:int
    redes_sociales:List[redes]