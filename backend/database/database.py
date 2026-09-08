import psycopg2

import os

from dotenv import load_dotenv

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()

DATABASE_URL = f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:5432/{os.getenv('POSTGRES_DB')}"

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass