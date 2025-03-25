from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, IPvAnyAddress, SecretStr
from dotenv import load_dotenv

from os import getenv

load_dotenv()


class DBSettings(BaseSettings):

    DB_DRIVER: str
    DB_USER: str
    DB_PASSWORD: SecretStr
    DB_HOST__: IPvAnyAddress = Field(validation_alias='DB_HOST')
    DB_PORT: int = Field(gt=0, le=65536)
    DB_NAME: str

    model_config = SettingsConfigDict(env_file='.env')

    @property
    def DB_HOST(self) -> str:
        return str(self.DB_HOST__)


settings = DBSettings()

print(settings.model_dump())
print(str(settings.DB_HOST))

