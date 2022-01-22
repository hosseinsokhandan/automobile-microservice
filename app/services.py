from models import AutomobileModel


class AutomobileService:
    async def get(self, id: int):
        return await AutomobileModel.get(id=id)


automobile_service = AutomobileService()
