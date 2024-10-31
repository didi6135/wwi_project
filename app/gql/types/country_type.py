from graphene import ObjectType, Int, String


class CountyType(ObjectType):
    country_id = Int()
    country_name = String()



