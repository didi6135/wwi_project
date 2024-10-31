from graphene import ObjectType, Int, String, Float


class CountyType(ObjectType):
    country_id = Int()
    country_name = String()

    # Relationship to the Country table
    # country = relationship("Country", back_populates="cities")
    # Relationship to the Target table
    # targets = relationship("Target", back_populates="city")

