import logging
import sys

from fastapi import FastAPI

from uvicorn import run

from api.v1.routers.user import router as user_router
from api.v1.routers.employer import router as employer_router



app = FastAPI()
# Регистрируем роутеры
[app.include_router(this_router) for this_router in (user_router, employer_router,)]



if __name__ == '__main__':
    run('main:app', reload=True)

'''
crud?
log
try except
dao
'''
