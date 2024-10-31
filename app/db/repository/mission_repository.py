from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from app.db.database import session_maker
from app.db.modeles import Mission, Target, Country, City

def get_all_missions():
    try:
        with session_maker() as session:
            return session.query(Mission).all()
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        return False

def get_mission_by_id(mission_id):
    try:
        with session_maker() as session:
            return session.query(Mission).filter_by(mission_id=mission_id).first()
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        return False

def get_missions_between_dates(start_date, end_date):
    try:
        with session_maker() as session:
            return session.query(Mission).filter(Mission.mission_date.between(start_date, end_date)).all()
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        return False

def get_missions_by_county_name(country_name):
    try:
        with session_maker() as session:
            return session.query(Mission).join(Mission.targets).join(Target.city).join(City.country).filter(Country.country_name == country_name).all()
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        return False

def get_missions_by_target_industry(industry: str):
    try:
        with session_maker() as session:
            return session.query(Mission).join(Mission.targets).filter(Target.target_industry == industry).all()
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        return False

def add_new_mission(mission_data):
    try:
        with session_maker() as session:
            mission_id = session.query(func.max(Mission.mission_id)).scalar() + 1
            new_mission = Mission(**mission_data, mission_id=mission_id)
            session.add(new_mission)
            session.commit()
            return new_mission
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        return False

def update_mission_by_id(mission_id, attack_result_data):
    try:
        with session_maker() as session:
            attack_result = session.query(Mission).filter_by(mission_id=mission_id).first()
            if not attack_result:
                raise Exception("Mission result not found")
            for key, value in attack_result_data.items():
                setattr(attack_result, key, value)
            session.commit()
            return attack_result
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        return False

def delete_mission(mission_id):
    try:
        with session_maker() as session:
            mission = session.query(Mission).filter_by(mission_id=mission_id).first()
            if not mission:
                raise Exception("Mission not found")
            session.query(Target).filter_by(mission_id=mission_id).delete()
            session.query(Mission).filter_by(mission_id=mission_id).delete()
            session.delete(mission)
            session.commit()
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        return False
