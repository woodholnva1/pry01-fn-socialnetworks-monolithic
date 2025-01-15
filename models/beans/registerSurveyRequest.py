from typing import List
from pydantic import BaseModel, Field, PositiveInt, validator, field_validator


class redes(BaseModel):
    id_red:PositiveInt = None
    value:PositiveInt  = None

class RegisterSurveyRequset(BaseModel):
    mail:str = Field(..., min_length=1)
    years:str = Field(..., min_length=1)
    sex:PositiveInt
    favorite_network:PositiveInt
    redes_sociales:List[redes]

    @field_validator("redes_sociales")
    def validar_lista_no_vacia(cls, v):
        if not v:
            raise ValueError("La lista de redes sociales no puede estar vacía")
        return v