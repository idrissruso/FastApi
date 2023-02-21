from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_NAME: str
    DATABASE_HOSTNAME: str
    DATABASE_PORT: str
    DATABASE_PASSWORD: str
    DATABASE_USERNAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MUNITES: int

    class Config:
        env_file = ".env"

settings = Settings()
