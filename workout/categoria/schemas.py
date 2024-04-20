from workout.contrib.schemas import BaseSchema
from pydantic import UUID4, Field
from typing import Annotated

class CategoriaIn(BaseSchema):
    nome:Annotated[str,Field(description='Nome da categoria',example='Scale',max_length=25)]

class CategoriaOut(CategoriaIn):
    id:Annotated[UUID4,Field(description='Identificador da categoria')]