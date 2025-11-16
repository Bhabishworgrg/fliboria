from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TITLE: str = 'Fliboria'
    API_STR: str = '/api/v1'
    DATABASE_URI: str

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()
