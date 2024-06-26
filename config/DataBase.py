from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker;
from sqlalchemy.ext.declarative import declarative_base;

DATABASE_URL = "postgresql://neondb_owner:kKeybHoTl71M@ep-winter-heart-a5dyxtzc.us-east-2.aws.neon.tech/neondb?sslmode=require&options=endpoint%3Dep-winter-heart-a5dyxtzc"

engine = create_engine(DATABASE_URL);

SessionLocal = sessionmaker(
    autocommit= False,
    autoflush=False,
    bind=engine
);

Base = declarative_base();