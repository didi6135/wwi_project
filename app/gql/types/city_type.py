from graphene import ObjectType, Int, String, Float, Field

from app.db.repository.countries_repository import get_country_by_id
from app.gql.types.country_type import CountyType


class CityType(ObjectType):
    city_id = Int()
    city_name = String()
    country_id = Int()
    latitude = Float()
    longitude = Float()

    country = Field(lambda: CountyType)

    @staticmethod
    def resolve_country(root, info):
        return get_country_by_id(root.country_id)
