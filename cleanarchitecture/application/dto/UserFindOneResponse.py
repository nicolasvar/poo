from pydantic import BaseModel

class UserFindOneResponse(BaseModel):
    id: int = 0
    name: str = ""
    email: str = ""