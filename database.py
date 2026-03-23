from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
from sqlmodel import create_engine, SQLModel

database_url = "postgresql://macbook:1320@localhost:5432/fastapi_db"
engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    ''' With this dependency, you can just add "db: Session = Depends(get_db)"
      to any route and it will give you a database session to work with 
      that is automatically closed after the request is done. 
      And with the middleware we have in place, the session will already 
      be set to the correct schema for the organization making the request.'''
    db = SessionLocal()
    try:
        yield db  # This 'hands over' the session to your route
    finally:
        db.close() # This runs AFTER the route is finished