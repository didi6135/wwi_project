from graphene import ObjectType

from app.gql.queries.city_queries import CityQueries
from app.gql.queries.country_queries import CountryQueries
from app.gql.queries.mission_queries import MissionQueries


class Query(CityQueries, CountryQueries, MissionQueries, ObjectType):
    pass