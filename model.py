from pydantic import BaseModel

class ITopNResponse(BaseModel):
    data: int

