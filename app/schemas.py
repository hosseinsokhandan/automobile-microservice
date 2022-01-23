from pydantic import BaseModel


class AutomobileInSchema(BaseModel):
    name: str
    type: str
    model: str
    manufacturer: str

class AutomobileOutSchema(BaseModel):
    id: int
    name: str
    type: str
    model: str
    manufacturer: str
