import logging
import sys

from typing import Annotated

from datetime import datetime

from fastapi import FastAPI, Depends, Header, status
from uvicorn import run

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker, Session


from models.users import UserBaseSchema, OptionalUserBaseSchema

from config.settings import settings
from db.models import Base, User


DB_STRING = URL.create(drivername=settings.DB_DRIVER,
                       username=settings.DB_USER,
                       password=settings.DB_PASSWORD.get_secret_value(),
                       host=settings.DB_HOST,
                       port=settings.DB_PORT,
                       database=settings.DB_NAME)


engine = create_engine(DB_STRING)

Base.metadata.reflect(engine)

app = FastAPI()

Session_ = sessionmaker(bind=engine)


def get_session():
    with Session_.begin() as session:
        yield session


@app.get('/')
def get(user_id: Annotated[int, Header()],
        session: Annotated[Session, Depends(get_session)]):
    user = session.get(User, user_id)
    if not user:
        return {'msg': 'not found'}
    return UserBaseSchema(**user.__dict__)


@app.post('/', status_code=200)
def insert_(user: UserBaseSchema,
            session: Annotated[Session, Depends(get_session)]):
    user = User(**user.model_dump())
    session.add(user)


@app.delete("/{user_id}", status_code=200)
def delete(user_id: int,
           session: Annotated[Session, Depends(get_session)]):
    user = session.get(User, user_id)
    if not user:
        return status.HTTP_204_NO_CONTENT
    session.delete(user)


@app.put('/{user_id}', status_code=200)
def put(user_id: int,
        user: OptionalUserBaseSchema,
        session: Annotated[Session, Depends(get_session)]):
    data = user.__dict__
    data['updated_at'] = datetime.now()
    session.query(User).filter(User.user_id == user_id).update(data)


if __name__ == '__main__':
    run('main:app', reload=True)

'''
crud?
log
try except
dao
'''
