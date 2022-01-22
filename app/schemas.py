from pydantic import BaseModel


class AutomobileOutSchema(BaseModel):
    id: int
    name: str
    type: str
    model: str
    manufacturer: str
