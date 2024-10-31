from graphene import ObjectType, Int, Float, Date, InputObjectType


class MissionType(ObjectType):
    mission_id = Int()
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()



class MissionInputType(InputObjectType):
    mission_date = Date()
    airborne_aircraft = Float(default_value=None)
    attacking_aircraft = Float(default_value=None)
    bombing_aircraft = Float(default_value=None)
    aircraft_returned = Float(default_value=None)
    aircraft_failed = Float(default_value=None)
    aircraft_damaged = Float(default_value=None)
    aircraft_lost = Float(default_value=None)

