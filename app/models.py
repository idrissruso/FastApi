import sys
sys.path.append('./')
from database import Base
from sqlalchemy import Column, Integer, String




class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
