from pydantic import BaseModel

class UserUpdateRequest(BaseModel):
    id:int
    name:str = ""
    email:str = ""