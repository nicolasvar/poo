from pydantic import BaseModel


class UserFindOneResponse(BaseModel):
    id: int
    name: str
    email: str 

