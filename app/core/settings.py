from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file_encoding="utf-8")

    auth_service_url: str


settings = Settings()
