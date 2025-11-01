# Connects SQLAlchemy to PostgreSQL using the URL from .env
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Engine manages the actual connection pool to the database
engine = create_engine(DATABASE_URL)
# SessionLocal lets you open/close DB sessions per API call
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base is inherited by all ORM models (like SymptomLog)
Base = declarative_base()
