from pydantic import BaseModel

class Exhibit(BaseModel):
    id: int
    name: str
    artist: str

class User(BaseModel):
    username: str
    password: str