from config.DataBase import Base;
from sqlalchemy import String,Column,Integer;


class User(Base):
    
    __tablename__ = "user";
    
    userId = Column(Integer,autoincrement=True,primary_key=True,nullable=False);
    name = Column(String,nullable=False,unique=True);
    password = Column(String,nullable=False);