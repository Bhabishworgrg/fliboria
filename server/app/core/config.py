from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_STR: str = '/api/v1'
    DATABASE_URI: str

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()
