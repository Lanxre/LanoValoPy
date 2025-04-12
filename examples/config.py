from pydantic_settings import BaseSettings, SettingsConfigDict

# ONLY FOR EXAMPLE USE
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    henrik_api_token: str