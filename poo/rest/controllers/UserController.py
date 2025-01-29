import logging
from typing import List 

from classy_fastapi import Routable, get, post, put, patch
from fastapi import FastAPI, Response
from tomlkit import items

from controllers.dto.UserFindOneResponse import UserFindOneResponse
from controllers.entity.UserEntity import UserEntity
from controllers.dto.Update import Update

class UserController(Routable):
    logger: logging.Logger
    app:FastAPI
    items :List[UserEntity] = [] 

    def __init__(self,app:FastAPI) -> None:
        super().__init__(prefix="/user")
        self.app = app
        self.app.include_router(self.router)
        self.logger = logging.getLogger(__name__)
        self.logger.info("UserController initialized")

    @get("/findone/{id}")
    def find_one(self, id:int) -> UserFindOneResponse:
        if id == 0:
            return {"error": "invalid id"}
        else:
            if(self.items == []):
                return {"error": "No items found"}
            else: 
                return self.items[id]
       #return UserFindOneResponse(id=id,name="Nicolas",email="nikovargas54@gmail.com")
    @post("/add")
    def add(self, id:int, name:str, email:str) -> Response:
        user = UserEntity(id=id, name=name,email=email)
        self.items.append(user)
        self.item = next((item for item in items if item.id == id), None)
        return Response(message="User added", success=True)
    
  #  @put("/update/{id}")
   # def update(self, id:int, name:str) -> Update:
    #    self.logger.info(f"Actualizando name con el id {id}: {name}")
     #   return Update(id=id, name=name, email=name.email)
    
   # @patch("/patch/{id}")
    #def patch(self, id:int, name:str) -> Patch:
        
