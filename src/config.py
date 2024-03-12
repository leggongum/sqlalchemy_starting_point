from pydantic_settings import BaseSettings, SettingsConfigDict

from typing import Literal

class Settings(BaseSettings):
    DB_MODE: Literal['dev', 'prod'] = 'dev'

    DB_HOST: str = 'localhost'
    DB_USER: str | None = None
    DB_PASS: str | None = None
    DB_NAME: str = 'test'

    ... # other enviroment paramets...

    @property
    def DB_URL_POSTGRES(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}/{self.DB_NAME}'
    
    @property
    def DB_URL_SQLite(self):
        return f'sqlite+aiosqlite:///./{self.DB_NAME}.db'
    
    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()
