from graphene import Mutation, Boolean, Field, Int

from app.db.repository.target_repository import add_new_target
from app.gql.types.target_type import TargetInputType, TargetType


class AddTarget(Mutation):
    class Arguments:
        mission_id = Int(required=True)
        target_data = TargetInputType(required=True)

    ok = Boolean()
    target = Field(TargetType)

    @staticmethod
    def mutate(root, info, target_data, mission_id):
        new_target = add_new_target(target_data, mission_id)
        return AddTarget(target=new_target, ok=True)
