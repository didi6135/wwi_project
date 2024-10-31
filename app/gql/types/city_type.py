from graphene import ObjectType, Int, String, Float


class CityType(ObjectType):
    city_id = Int()
    city_name = String()
    country_id = Int()
    latitude = Float()
    longitude = Float()

    # Relationship to the Country table
    # country = relationship("Country", back_populates="cities")
    # Relationship to the Target table
    # targets = relationship("Target", back_populates="city")

