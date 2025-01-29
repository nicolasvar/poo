from pydantic import BaseModel, EmailStr

class Update(BaseModel):

    name: str
    email: EmailStr