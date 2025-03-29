from datetime import datetime
from typing import Optional, Annotated
from pydantic import BaseModel, EmailStr, Field



class GetUserSchemaResponse(BaseModel):
    """
    ## Схема ответа для получения данных пользователя.

    Модель для представления данных пользователя в ответе API.

    Args:
        BaseModel (BaseModel): Базовый класс для создания схем валидации данных.

    Attributes:
        id (int): Уникальный идентификатор пользователя.
        username (str): Имя пользователя.
        email (EmailStr): Электронная почта пользователя.
        first_name (Optional[str]): Имя пользователя, необязательное поле с ограничениями по длине.
        last_name (Optional[str]): Фамилия пользователя, необязательное поле с ограничениями по длине.
        is_active (bool): Статус активности пользователя.
        created_at (Optional[datetime]): Дата и время создания пользователя, необязательное поле.
        updated_at (Optional[datetime]): Дата и время последнего обновления пользователя, необязательное поле.
    """ 
    id: int
    username: str
    email: EmailStr
    first_name: Annotated[Optional[str], Field(None, min_length=2, max_length=50)]
    last_name: Annotated[Optional[str], Field(None, min_length=2, max_length=50)]
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None