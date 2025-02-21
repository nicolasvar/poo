from pydantic import BaseModel

class UserFindAllResponse(BaseModel):
    id: int = 0
    name:str = ""
    email: str = ""