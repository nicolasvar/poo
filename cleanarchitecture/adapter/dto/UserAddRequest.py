from pydantic import BaseModel


class UserAddRequest (BaseModel):
    id:int
    username:str
    email:str