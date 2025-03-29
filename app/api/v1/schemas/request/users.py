from typing import Annotated, Optional
from pydantic import BaseModel, EmailStr, Field



class AddUserSchemaRequest(BaseModel):
    """
    ## Схема запроса для добавления пользователя.

    Модель для валидации данных, необходимых для создания нового пользователя.

    Args:
        BaseModel (BaseModel): Базовый класс для создания схем валидации данных.

    Attributes:
        username (str): Имя пользователя, обязательное поле.
        email (EmailStr): Электронная почта пользователя, обязательное поле.
        first_name (Optional[str]): Имя пользователя, необязательное поле с ограничениями по длине.
        last_name (Optional[str]): Фамилия пользователя, необязательное поле с ограничениями по длине.
        is_active (bool): Статус активности пользователя, обязательное поле.
    """
    username: str
    email: EmailStr
    first_name: Annotated[Optional[str], Field(None, min_length=2, max_length=50)]
    last_name: Annotated[Optional[str], Field(None, min_length=2, max_length=50)]
    is_active: bool
    
    

class PutOptionalUserBaseSchema(BaseModel):
    """
    ## Схема для обновления данных пользователя.

    Модель для валидации данных, которые могут быть обновлены для существующего пользователя.
    
    Args:
        BaseModel (BaseModel): Базовый класс для создания схем валидации данных.

    Attributes:
        username (Optional[str]): Имя пользователя, необязательное поле с ограничениями по длине.
        email (Optional[EmailStr]): Электронная почта пользователя, необязательное поле с валидацией формата.
        first_name (Optional[str]): Имя пользователя, необязательное поле с ограничениями по длине.
        last_name (Optional[str]): Фамилия пользователя, необязательное поле с ограничениями по длине.
        is_active (Optional[bool]): Статус активности пользователя, необязательное поле.
    """   
    username: Annotated[Optional[str], Field(None, min_length=2, max_length=50)]
    email: Optional[EmailStr] = None
    first_name: Annotated[Optional[str], Field(None, min_length=2, max_length=50)]
    last_name: Annotated[Optional[str], Field(None, min_length=2, max_length=50)]
    is_active: Optional[bool] = None