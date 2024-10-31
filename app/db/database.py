from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session

from app.settings.config import DB_URL

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine, expire_on_commit=False)

# command to fix the id of missions table
# CREATE SEQUENCE IF NOT EXISTS missions_mission_id_seq;
# ALTER TABLE missions ALTER COLUMN mission_id SET DEFAULT nextval('missions_mission_id_seq');
# SELECT setval('missions_mission_id_seq', COALESCE((SELECT MAX(mission_id) FROM missions) + 1, 1), false);