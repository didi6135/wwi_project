from graphene import ObjectType, List, Field, Int, Date, String
from app.db.repository.mission_repository import get_all_missions, get_mission_by_id, get_missions_between_dates, \
    get_missions_by_county_name, get_missions_by_target_industry
from app.db.repository.target_type_repository import get_mission_results_by_type
from app.gql.types.mission_type import MissionType


class MissionQueries(ObjectType):
    missions = List(MissionType)

    mission_by_id = Field(MissionType, mission_id=Int(required=True))

    missions_between_dates = List(MissionType, start_date=Date(required=True), end_date=Date(required=True))

    missions_by_country = List(MissionType, country_name=String(required=True))

    missions_by_target_industry = List(MissionType, target_industry=String(required=True))

    mission_results_by_type = List(MissionType, attack_type=String(required=True))

    @staticmethod
    def resolve_missions(root, info):
        return get_all_missions()

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        return get_mission_by_id(mission_id)

    @staticmethod
    def resolve_missions_between_dates(root, info, start_date, end_date):
        return get_missions_between_dates(start_date, end_date)

    @staticmethod
    def resolve_missions_by_country(root, info, country_name):
        return get_missions_by_county_name(country_name)

    @staticmethod
    def resolve_missions_by_target_industry(root, info, target_industry):
        return  get_missions_by_target_industry(target_industry)

    @staticmethod
    def resolve_mission_results_by_type(root, info, attack_type):
        return get_mission_results_by_type(attack_type)