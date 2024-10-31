from graphene import ObjectType, List
from app.db.repository.countries_repository import get_all_countries
from app.gql.types.country_type import CountyType


class CountryQueries(ObjectType):
    countries = List(CountyType)

    @staticmethod
    def resolve_countries(root, info):
        return get_all_countries()