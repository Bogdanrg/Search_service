from pydantic_settings import BaseSettings, SettingsConfigDict


class ZookeeperSettings(BaseSettings):
    CLIENT_PORT: int
    TICK_TIME: int

    model_config = SettingsConfigDict(env_prefix="ZOOKEEPER_", env_file=".env")


class KafkaSettings(BaseSettings):
    BROKER_ID: int
    ZOOKEEPER_CONNECT: str
    ADVERTISED_LISTENERS: str
    LISTENER_SECURITY_PROTOCOL_MAP: str
    INTER_BROKER_LISTENER_NAME: str
    OFFSETS_TOPIC_REPLICATION_FACTOR: int
    TOPIC_NAME: str
    PORTS: str
    BOOTSTRAP_SERVER: str

    model_config = SettingsConfigDict(env_prefix="KAFKA_", env_file=".env")


class ESSettings(BaseSettings):
    PORTS: int
    URL: str
    HOST: str
    PORT: int
    SCHEME: str

    model_config = SettingsConfigDict(env_prefix="ES_", env_file=".env")


class AppSettings(BaseSettings):
    UVICORN_HOST: str
    UVICORN_PORT: int
    BACKEND_HOST: int
    BACKEND_CONT: int
    TITLE: str

    model_config = SettingsConfigDict(env_prefix="APP_", env_file=".env")


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    kafka: KafkaSettings = KafkaSettings()
    zookeeper: ZookeeperSettings = ZookeeperSettings()
    es: ESSettings = ESSettings()


settings = Settings()
