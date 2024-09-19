from os import getenv

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

load_dotenv()

is_prod: bool = bool(getenv("is_prod", default=False))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file_encoding="utf-8")

    auth_service_url: str
    is_prod: str
    upload_bucket_name: str
    minio_endpoint: str
    minio_access_key: str
    minio_secret_key: str


settings = Settings()
