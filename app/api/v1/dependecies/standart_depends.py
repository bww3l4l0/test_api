from typing import Generator

from db.sessions import Session_
from sqlalchemy.orm import Session



def get_session() -> Generator[Session]:
    """
    ## Получение сессии базы данных.

    Функция-генератор, которая создает и возвращает сессию для работы с базой данных.
    Сессия автоматически закрывается после завершения работы с ней.

    Yields:
        Generator[Session]: Генератор, который возвращает объект сессии 
        для выполнения операций с базой данных.
    """  
    with Session_.begin() as session:
        yield session