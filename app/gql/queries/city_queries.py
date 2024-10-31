from graphene import ObjectType, List, String

from app.db.repository.city_repository import get_all_cities
from app.gql.types.city_type import CityType
from app.gql.types.mission_type import MissionType


class CityQueries(ObjectType):
    cities = List(CityType)

    mission_statistics_by_city = List(MissionType, country_name=String(required=True))

    @staticmethod
    def resolve_cities(root, info):
        return get_all_cities()


