from fastapi import APIRouter
from schemas import AutomobileInSchema, AutomobileOutSchema
from services import automobile_service


router = APIRouter()


@router.get("/populate")
async def generate_data():
    await automobile_service._delete_all()
    await automobile_service.create(
        AutomobileInSchema(
            type="SEDAN", model="Camaro SS 2019",
            manufacturer="Chevrolet"
        )
    )
    await automobile_service.create(
        AutomobileInSchema(
            type="SPORT", model="Ford GT 2006",
            manufacturer="Ford Motor Company"
        )
    )
    await automobile_service.create(
        AutomobileInSchema(
            type="COUPE", model="Mustang 2017",
            manufacturer="Ford Motor Company"
        )
    )
    return {"message": "Populated."}


@router.get("/{id}", response_model=AutomobileOutSchema)
async def get(id: int):
    return await automobile_service.get(id)
