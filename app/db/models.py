
from typing import Optional
from datetime import datetime

from sqlalchemy import BigInteger, String, Boolean, DateTime, func
from sqlalchemy.orm import declarative_base, mapped_column, Mapped

from .table_name_maps import TableNames



Base = declarative_base()



class User(Base):
    __tablename__ = TableNames.USERS_TABLE_NAME

    # user_id: Mapped[Integer] = mapped_column(Integer, primary_key=True)  # старая твоя версия
    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50))  # рекомендую сделать Mapped[Optional[str]]
    email: Mapped[str] = mapped_column(String(100))
    first_name: Mapped[Optional[str]] = mapped_column(String(50))  # рекомендую сделать Mapped[Optional[str]]
    last_name: Mapped[Optional[str]] = mapped_column(String(50))  # рекомендую сделать Mapped[Optional[str]]
    is_active_qwerty: Mapped[bool] = mapped_column(Boolean)  # рекомендую сделать Mapped[Optional[bool]]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now())
