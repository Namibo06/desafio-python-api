from pydantic import UUID4, Field,PositiveFloat
from typing import Annotated
from workout.contrib.schemas import BaseSchema

class CentroTreinamentoIn(BaseSchema):
    nome:Annotated[str,Field(description='Nome do Centro de Treinamento',example='CT King',max_length=20)]
    endereco:Annotated[str,Field(description='Endereço do Centro de Treinamento',example='Rua X Quadra 2',max_length=60)]
    proprietario:Annotated[str,Field(description='Nome do Proprietario do Centro de Treinamento',example='Lili',max_length=30)]

class CentroTreinamentoAtleta(BaseSchema):
     nome:Annotated[str,Field(description='Nome do Centro de Treinamento',example='CT King',max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
     id: Annotated[UUID4,Field(description="Idetificador do centro de treinamento")]