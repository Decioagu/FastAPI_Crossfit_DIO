from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)

    atleta: Mapped['AtletaModel'] = relationship(back_populates="categoria")