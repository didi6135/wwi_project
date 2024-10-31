from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session

from app.settings.config import DB_URL

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine, expire_on_commit=False)
