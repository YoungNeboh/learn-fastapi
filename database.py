# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
from sqlmodel import create_engine, SQLModel

database_url = "postgresql://macbook:1320@localhost:5432/fastapi_db"
engine = create_engine(database_url)

