from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

database_url = "postgresql://macbook:1320@localhost:5432/fastapi_db"
engine = create_engine(database_url)
SessionLocal = sessionmaker(autoflush=False, autoCommit=False, bind=engine)
