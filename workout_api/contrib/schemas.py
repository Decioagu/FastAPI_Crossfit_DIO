from typing import Annotated
from pydantic import UUID4, BaseModel, Field
from datetime import datetime


class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True

'''
Classe do FastAPI para o pydantic
Esta classe vai gerar id único para as demais classes: tabelas atleta, categoria e centro_treinamento
UUID4 valida strings de 16 caracteres alfanuméricos aleatórios enviado por uuid4()
Enviados pelo controller.py
'''
class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(description='Identificador')]
    created_at: Annotated[datetime, Field(description='Data de criação')]         