from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    DB_URL: Optional[str]

    # Loads the dotenv file
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
