import sys
sys.path.append('./')
from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String,DateTime, func



class Users(Base):
    __tablename__ = "Users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    __table_args__ = {"extend_existing": True}


class Post(Base):
    __tablename__ = "Posts"
    post_id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String,nullable=False,unique=True)
    content = Column(String,nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    owner_id = Column(Integer,ForeignKey("Users.user_id",ondelete="CASCADE"))
    __table_args__ = {"extend_existing": True}