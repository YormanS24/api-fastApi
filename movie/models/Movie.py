from config.DataBase import Base;
from sqlalchemy.orm import relationship;
from sqlalchemy import Integer,String,Column,ForeignKey;

class Movie(Base):
    
    __tablename__ = "movie";
    
    movieId =  Column(Integer,autoincrement=True,primary_key=True,nullable=False);
    name = Column(String,nullable=False,unique=True);
    description = Column(String);
    
    categoryId = Column(Integer,ForeignKey('category.categoryId'));
    
    category = relationship("Category",back_populates="movies");
    