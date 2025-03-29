from typing import Annotated

from datetime import datetime

from fastapi.routing import APIRouter
from fastapi import status
from fastapi import Depends, Header

from sqlalchemy.orm import Session

from api.v1.schemas.response.users import GetUserSchemaResponse
from api.v1.schemas.request.users import AddUserSchemaRequest, PutOptionalUserBaseSchema

from api.v1.dependecies.standart_depends import get_session

from db.models import User



router = APIRouter(prefix='/v1/users', tags=['Работа с пользователями', 'v1'])



@router.get(
    '/get_user',
    response_model=GetUserSchemaResponse  # Здесь я сам добавил модель
    # response_model=SomeModel  
)
def get_user(
    user_id: Annotated[int, Header()],
    session: Annotated[Session, Depends(get_session)]
):
    """
    ## Получает пользователя по его идентификатору.

    ### Args:
        user_id (Annotated[int, Header]): Идентификатор пользователя, передаваемый в заголовке.
        session (Annotated[Session, Depends]): Сессия базы данных.

    ### Returns:
        GetUserSchemaResponse: Данные пользователя в виде схемы.
    """   
    user = session.get(User, user_id)
    if not user:
        return {'msg': 'not found'}
    return GetUserSchemaResponse(**user.__dict__)


@router.post(
    '/add_user',
    status_code=200,
    # response_model=SomeModel  # у тебя отсутствует какая-либо модель ответа    
)
def insert_(
    user: AddUserSchemaRequest,
    session: Annotated[Session, Depends(get_session)]
):
    """
    ### Добавляет нового пользователя в базу данных.

    Args:
        user (AddUserSchemaRequest): Данные пользователя для добавления.
        session (Annotated[Session, Depends]): Сессия базы данных.

    Returns:
        UserBaseSchema: Данные добавленного пользователя в виде схемы.
    """    
    user = User(**user.model_dump())
    session.add(user)
    # При вставке нужно вернуть вставленные данные


@router.delete(
    "/{user_id}",
    status_code=200,
    # response_model=SomeModel  # у тебя отсутствует какая-либо модель ответа
)
def delete(
    user_id: int,
    session: Annotated[Session, Depends(get_session)]
):
    """
    # Удаляет пользователя по его идентификатору.

    ### Args:
        user_id (int): Идентификатор пользователя для удаления.
        session (Annotated[Session, Depends]): Сессия базы данных.

    ### Returns:
        status.HTTP_204_NO_CONTENT: Если пользователь не найден.
    """    
    user = session.get(User, user_id)
    if not user:
        return status.HTTP_204_NO_CONTENT
    session.delete(user)
    # При удалении нужно вернуть удалённые данные


@router.put(
    '/{user_id}',
    status_code=200,
    # response_model=SomeModel  # у тебя отсутствует какая-либо модель ответа
)
def put(
    user_id: int,
    user: PutOptionalUserBaseSchema,
    session: Annotated[Session, Depends(get_session)]
):
    """
    ## Обновляет данные пользователя по его идентификатору.

    ### Args:
        user_id (int): Идентификатор пользователя для обновления.
        user (PutOptionalUserBaseSchema): Данные для обновления.
        session (Annotated[Session, Depends]): Сессия базы данных.

    ### Returns:
        UserBaseSchema: Обновлённые данные пользователя в виде схемы.
    """  
    data = user.__dict__
    data['updated_at'] = datetime.now()
    session.query(User).filter(User.user_id == user_id).update(data)
    # При обновлении нужно вернуть обновленные данные данные