from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ZOOKEEPER_CLIENT_PORT: int
    ZOOKEEPER_TICK_TIME: int
    KAFKA_BROKER_ID: int
    KAFKA_ZOOKEEPER_CONNECT: str
    KAFKA_ADVERTISED_LISTENERS: str
    KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: str
    KAFKA_INTER_BROKER_LISTENER_NAME: str
    KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: int
    KAFKA_TOPIC_NAME: str
    BOOTSTRAP_SERVER: str
    UVICORN_HOST: str
    UVICORN_PORT: int
    BACKEND_HOST: int
    BACKEND_CONT: int
    ES_PORTS: int
    APP_TITLE: str
    ES_URL: str
    ES_HOST: str
    ES_PORT: int
    SCHEME: str
    KAFKA_PORTS: int
    ZOOKEEPER_PORTS: int

    model_config = SettingsConfigDict(env_file=".env")


app_settings = Settings()
