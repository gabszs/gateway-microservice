from dotenv import load_dotenv
from os import getenv
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

load_dotenv()

develop_env: bool = getenv("develop_env")

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file_encoding="utf-8")

    auth_service_url: str
    develop_env: str
    minio_endpoint: str
    minio_access_key: str
    minio_secret_key: str
    minio_bucket: str

settings = Settings()
