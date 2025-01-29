from pydantic import BaseModel


class UserEntity(BaseModel):
    id:int
    name: str
    email:str