from pydantic import BaseModel

class UserEntity(BaseModel):
    id:int = 0
    name: str = ""
    email: str = ""
    password: str = ""
