from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    APP_NAME: str = "AI Creative Content Generator"
    DEBUG: bool = False
    VERSION: str = "0.1.0"

    class Config:
        env_file = ".env"


settings = AppSettings()
