from app.db.database import session_maker
from app.db.modeles import Target


def add_new_target(target_data, mission_id):

    with session_maker() as session:
        new_target = Target(**target_data, mission_id=mission_id)
        session.add(new_target)
        session.commit()
        return new_target