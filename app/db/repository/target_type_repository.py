from app.db.database import session_maker
from app.db.modeles import Mission, Target
from app.db.modeles.target_type import TargetType


def get_mission_results_by_type(attack_type: str):
    with session_maker() as session:
        return (
            session.query(Mission)
            .join(Target, Mission.mission_id == Target.mission_id)
            .join(TargetType, Target.target_type_id == TargetType.target_type_id)
            .filter(TargetType.target_type_name == attack_type)
            .all()
        )

