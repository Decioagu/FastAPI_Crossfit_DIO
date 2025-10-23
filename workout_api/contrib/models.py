from uuid import uuid4 # criar IDs únicos
from sqlalchemy import UUID # Importa o tipo genérico UUID do SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column # declarar modelos
from sqlalchemy.dialects.postgresql import UUID as PG_UUID # importando o tipo UUID específico do PostgreSQL

# regar identificador único
class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, nullable=False) 