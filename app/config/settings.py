from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, IPvAnyAddress, SecretStr
from dotenv import load_dotenv

from os import getenv

load_dotenv()


class DBSettings(BaseSettings):
    """
    ## Настройки базы данных.

    Класс для управления настройками подключения к базе данных, 
    загружаемыми из переменных окружения.

    Args:
        BaseSettings (BaseSettings): Базовый класс для работы с настройками, 
        который обеспечивает автоматическую загрузку значений из переменных окружения.

    Attributes:
        DB_DRIVER (str): Драйвер базы данных (например, 'postgresql', 'mysql').
        DB_USER (str): Имя пользователя для подключения к базе данных.
        DB_PASSWORD (SecretStr): Пароль для подключения к базе данных, 
        который хранится в зашифрованном виде.
        DB_HOST__ (IPvAnyAddress): Адрес хоста базы данных, 
        который может быть как IPv4, так и IPv6.
        DB_PORT (int): Порт для подключения к базе данных, 
        должен быть в диапазоне от 1 до 65535.
        DB_NAME (str): Имя базы данных, к которой нужно подключиться.

    Returns:
        DBSettings: Экземпляр класса с загруженными настройками.
    """ 
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

