from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = Field(default="postgresql+asyncpg://postgres:Enigma.1@127.0.0.2:5432/workout")


settings = Settings()