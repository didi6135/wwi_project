from graphene import Mutation, Field, Boolean, Int

from app.db.repository.mission_repository import add_new_mission, update_mission_by_id, delete_mission
from app.gql.types.mission_type import MissionInputType, MissionType


class AddMission(Mutation):
    class Arguments:
        mission_data = MissionInputType()

    ok = Boolean()
    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_data):
        new_mission = add_new_mission(mission_data)
        if not new_mission:
            return AddMission(mission=None, ok=False)

        return AddMission(mission=new_mission, ok=True)



class UpdateMission(Mutation):
    class Arguments:
        mission_id = Int(required=True)
        attack_result_data = MissionInputType(required=True)

    ok = Boolean()
    attack_result = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_id, attack_result_data):
        update_mission = update_mission_by_id(mission_id, attack_result_data)
        if not update_mission:
            return UpdateMission(attack_result=None, ok=False)

        return UpdateMission(attack_result=update_mission, ok=True)



class DeleteMission(Mutation):
    class Arguments:
        mission_id = Int(required=True)

    ok = Boolean()

    @staticmethod
    def mutate(root, info, mission_id):
        deleted = delete_mission(mission_id)
        if not deleted:
            return DeleteMission(ok=False)

        return DeleteMission(ok=True)
