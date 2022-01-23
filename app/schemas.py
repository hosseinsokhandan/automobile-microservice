from pydantic import BaseModel


class AutomobileInSchema(BaseModel):
    type: str
    model: str
    manufacturer: str

class AutomobileOutSchema(BaseModel):
    id: int
    type: str
    model: str
    manufacturer: str
