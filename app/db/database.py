from sqlalchemy import create_engine, text, inspect
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, Session

from app.settings.config import DB_URL

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine, expire_on_commit=False)

# command to fix the id of missions table
# CREATE SEQUENCE IF NOT EXISTS missions_mission_id_seq;
# ALTER TABLE missions ALTER COLUMN mission_id SET DEFAULT nextval('missions_mission_id_seq');
# SELECT setval('missions_mission_id_seq', COALESCE((SELECT MAX(mission_id) FROM missions) + 1, 1), false);
init_sequence_sql = """
    CREATE SEQUENCE IF NOT EXISTS missions_mission_id_seq;
    ALTER TABLE missions ALTER COLUMN mission_id SET DEFAULT nextval('missions_mission_id_seq');
    SELECT setval('missions_mission_id_seq', COALESCE((SELECT MAX(mission_id) FROM missions) + 1, 1), false);
"""

def check_and_initialize_missions():
    try:
        # Check if the 'missions' table exists
        inspector = inspect(engine)
        if 'missions' not in inspector.get_table_names():
            print("The 'missions' table does not exist. Please check your setup scripts.")

        # Run initialization SQL if needed
        with engine.connect() as connection:
            connection.execute(text(init_sequence_sql))
            print("Initialization commands executed successfully.")
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")

# Run the check and initialize function
check_and_initialize_missions()