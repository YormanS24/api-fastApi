from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker;
from sqlalchemy.ext.declarative import declarative_base;

DATABASE_URL= "postgresql://neondb_owner:kKeybHoTl71M@ep-winter-heart-a5dyxtzc.us-east-2.aws.neon.tech/neondb?sslmode=require";

engine = create_engine(DATABASE_URL,echo=True);

SessionLocal = sessionmaker(
    autocommit= False,
    autoflush=False,
    bind=engine
);

Base = declarative_base();