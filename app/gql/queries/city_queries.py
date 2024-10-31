from graphene import ObjectType, List

from app.db.repository.city_repository import get_all_cities
from app.gql.types.city_type import CityType


class CityQueries(ObjectType):
    cities = List(CityType)

    @staticmethod
    def resolve_cities(root, info):
        return get_all_cities()