from pydantic import BaseModel


class Profile(BaseModel):
    email: str
    name: str
    contact: str

    class Config:
        orm_mode = True
