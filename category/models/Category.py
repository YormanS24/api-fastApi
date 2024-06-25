from config.DataBase import Base;
from sqlalchemy import Column,Integer,String;
from sqlalchemy.orm import relationship;

class Category(Base):
    __tablename__ = "category";
    
    categoryId = Column(Integer,primary_key=True,autoincrement=True);
    name = Column(String,nullable=False);
    description = Column(String,nullable=True);
    
    movies = relationship("Movie",back_populates="category");