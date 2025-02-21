from typing import Any
from pydantic import BaseModel


class Response(BaseModel):
    data: Any = None
    success: bool = False
    message: str = ""