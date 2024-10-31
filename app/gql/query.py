from graphene import ObjectType

from app.gql.queries.city_queries import CityQueries
from app.gql.queries.country_queries import CountryQueries


class Query(CityQueries, CountryQueries, ObjectType):
    pass