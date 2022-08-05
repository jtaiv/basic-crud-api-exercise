from pydantic import BaseModel, StrictStr


class Profile(BaseModel):
    email: StrictStr
    name: StrictStr
    contact: StrictStr

    class Config:
        orm_mode = True
