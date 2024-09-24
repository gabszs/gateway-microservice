from os import getenv
from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

load_dotenv()

env_path = None if bool(getenv("is_prod", default=False)) else "dev.env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_path, env_file_encoding="utf-8")

    auth_service_url: str
    is_prod: str
    upload_bucket_name: str

    minio_endpoint: str
    minio_access_key: str
    minio_secret_key: str

    RABBIT_URL: str
    RABBITMQ_USER: str
    RABBITMQ_PASS: str

    UPLOAD_ROUTING_KEY: str
    UPLOAD_EXCHANGE: Optional[str] = ""


settings = Settings()
