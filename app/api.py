from fastapi import APIRouter
from schemas import AutomobileOutSchema
from services import automobile_service


router = APIRouter()


@router.get("{id}", response_model=AutomobileOutSchema)
def get(id: int):
    return automobile_service.get(id)
