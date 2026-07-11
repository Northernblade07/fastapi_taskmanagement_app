# import os
# from dotenv import load_dotenv
# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker

# load_dotenv()

# USER = os.getenv("POSTGRES_USER", "user123")
# PASSWORD = os.getenv("POSTGRES_PASSWORD", "password123")
# HOST = os.getenv("POSTGRES_HOST", "localhost")
# PORT = os.getenv("POSTGRES_PORT", "5432")
# DB = os.getenv("POSTGRES_DB", "task_management_fastapi")

# DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.utils.settings import settings

Base = declarative_base()

engine = create_engine(url=settings.DB_CONNECTION)

LocalSession = sessionmaker(bind=engine)

def get_db():
    session = LocalSession()
    try:
        yield session
    finally:
        session.close()