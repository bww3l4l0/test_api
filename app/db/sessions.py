from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import settings
from db.models import Base



DB_STRING = URL.create(
    drivername=settings.DB_DRIVER,
    username=settings.DB_USER,
    password=settings.DB_PASSWORD.get_secret_value(),
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME
)


engine = create_engine(DB_STRING)

Base.metadata.reflect(engine)

Session_ = sessionmaker(bind=engine)