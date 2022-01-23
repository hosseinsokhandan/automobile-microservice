from schemas import AutomobileInSchema
from models import AutomobileModel


class AutomobileService:
    async def get(self, id: int) -> AutomobileModel:
        return await AutomobileModel.get(id=id)

    async def create(self, automobile: AutomobileInSchema):
        return await AutomobileModel.create(**dict(automobile))

    async def _delete_all(self):
        return await AutomobileModel.all().delete()


automobile_service = AutomobileService()
