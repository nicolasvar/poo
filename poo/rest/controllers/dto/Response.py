from pydantic import BaseModel


class Response(BaseModel):
    message:str
    data: None = None
    success:bool 