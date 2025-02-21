from classy_fastapi import Routable, get, patch, post, put
from tomlkit import item
from adapter.dto.UserAddRequest import UserAddRequest
from adapter.dto.UserUpdateRequest import UserUpdateRequest
from adapter.mapper.UserMapper import UserMaper
from domain.usecase.IUserAddUseCase import IUserAddUseCase
from domain.usecase.IUserUpdateUseCase import IUserUpdateUseCase
from domain.valueobject.Response import Response
from application.service.UserService import UserService
from domain.usecase.IUserFindOneUseCase import IUserFindOneUseCase
from domain.usecase.IUserFindAllUseCase import IUserFindAllUseCase
from infraestructure.UserRepository import UserRepository
from fastapi import FastAPI
import logging

class UserController(Routable):
    logger: logging.Logger
    app: FastAPI
    userFindOneUseCase: IUserFindOneUseCase
    userFindAllUseCase: IUserFindAllUseCase
    userAddUseCase: IUserAddUseCase
    userUpdateUseCase: IUserUpdateUseCase

    def __init__(self, app: FastAPI) -> None:
        super().__init__(prefix="/user")
        self.app=app
        self.app.include_router(self.router)
        self.logger = logging.getLogger(__name__)
        service = UserService(UserRepository())
        self.userFindOneUseCase = service
        self.userFindAllUseCase = service
        self.userAddUseCase = service
        self.userUpdateUseCase = service

    @get("/findone/{id}")    
    def findOne(self, id:int) -> Response:
        return self.userFindOneUseCase.findOne(id)
    
    @get("/findall")
    def findAll(self) ->Response:
        return self.userFindAllUseCase.findAll()
    
    @post("/add")
    def add(self, item: UserAddRequest)->Response:
        entity = UserMaper.toAddEntity(item)
        return self.userAddUseCase.add(entity)
    
    @put("/update")
    def update(self, item:UserUpdateRequest) -> Response:
        entity = UserMaper.toUpdateEntity(item)
        return self.userUpdateUseCase.update(entity)
    
    @patch("/updateemail")
    def updateEmail(self, email:str) -> Response:
        entity = UserMaper.toUpdateEmailEntity(item)
        return self.userUpdateEmailUseCase.updateEmail(entity)