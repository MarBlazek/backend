from pydantic import BaseModel

class Exhibit(BaseModel):
    id: int
    name: str
    artist: str