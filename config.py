from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_TITLE: str
    UVICORN_HOST: str
    UVICORN_PORT: int
    ES_URL: str
    ES_HOST: str
    ES_PORT: int

    model_config = SettingsConfigDict(env_file=".env")


app_settings = Settings()
