import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

PGUSER = os.getenv('POSTGRES_USER')
PGPASS = os.getenv('POSTGRES_PASSWORD')

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = f"postgresql://{PGUSER}:{PGPASS}@localhost/postgres"

# engine = create_engine(
#   SQLALCHEMY_DATABASE_URL, 
#   connect_args={"check_same_thread": False}
# )
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
