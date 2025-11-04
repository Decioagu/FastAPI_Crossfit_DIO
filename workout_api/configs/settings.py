from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = Field(default="postgresql+asyncpg://postgres:Enigma.1@127.0.0.1:5433/workout")


settings = Settings()