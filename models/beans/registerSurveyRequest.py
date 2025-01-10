from typing import List, Any
from pydantic import BaseModel


class RegisterSurveyRequset(BaseModel):
    mail:str
    years:str
    sex:str
    favorite_network:str
    redes_sociales:List[Any]