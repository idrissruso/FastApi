import sys

sys.path.append('./')
from database import Base
from sqlalchemy import Column, Integer, String, DATETIME, DateTime, func
import datetime


class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
