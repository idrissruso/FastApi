import sys
sys.path.append('./')
from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String,DateTime, func
from sqlalchemy.orm import relationship



class Users(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    __table_args__ = {"extend_existing": True}


class Post(Base):
    __tablename__ = "post"
    post_id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String,nullable=False,unique=True)
    content = Column(String,nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    owner_id = Column(Integer,ForeignKey("user.user_id",ondelete="CASCADE"))
    owner = relationship("app.models.Users")
    __table_args__ = {"extend_existing": True}
    
    
class Likes(Base):
    __tablename__ = "like"
    post_id = Column(Integer,ForeignKey("post.post_id",ondelete="CASCADE"),primary_key=True)
    user_id = Column(Integer,ForeignKey("user.user_id",ondelete="CASCADE"),primary_key=True)