from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlmodel import create_engine
from fastapi import Request

database_url = "postgresql://macbook:1320@localhost:5432/fastapi_db"
engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db(request: Request):
    ''' With this dependency, you can just add "db: Session = Depends(get_db)"
      to any route and it will give you a database session to work with 
      that is automatically closed after the request is done. 
      And with the middleware we have in place, the session will already 
      be set to the correct schema for the organization making the request.'''
    db = SessionLocal()
    # Pull the schema name we found in the middleware
    schema_name = getattr(request.state, "schema_name", "public")
    try:
        # Tell THIS specific session to use the tenant's schema
        db.execute(text(f"SET search_path TO {schema_name}, public"))
        yield db  # This 'hands over' the session to your route
    finally:
        db.close() # This runs AFTER the route is finished