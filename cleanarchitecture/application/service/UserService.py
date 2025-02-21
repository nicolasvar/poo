from typing import List
from domain.entity.DMLEntity import DMLEntity
from domain.entity.UserEntity import UserEntity
from domain.valueobject.Response import Response
from application.dto.UserFindAllResponse import UserFindAllResponse
from application.dto.UserFindOneResponse import UserFindOneResponse
from application.exceptions import DataNotFoundException
from application.service.BaseService import BaseService
from domain.usecase.IUserFindOneUseCase import IUserFindOneUseCase
from domain.usecase.IUserFindAllUseCase import IUserFindAllUseCase
from domain.usecase.IUserAddUseCase import IUserAddUseCase
from domain.repository.IUserRepository import IUserRepository


class UserService(BaseService,IUserFindOneUseCase, IUserFindAllUseCase, IUserAddUseCase):
    userRepository: IUserRepository

    def __init__(self, userRepository: IUserRepository):
        self.userRepository = userRepository
        
    def findOne(self, id:int)->Response:
        try:
            item = self.userRepository.findOne(id)
            if(item is None):
                raise DataNotFoundException("User not found")
            dto: UserFindOneResponse = UserFindOneResponse()
            dto.id = item.id
            dto.name = item.name
            dto.email = item.email
            return Response(data=dto, success=True, message="")
        except Exception as e:
            return Response(data=None, success=False, message=str(e))
    
    def findAll(self) -> Response:
        try:
            items = self.userRepository.findAll()
            dtos: List[UserFindAllResponse] = []
            for item in items:
                dto: UserFindAllResponse = UserFindAllResponse()
                dto.id = item.id
                dto.name = item.name
                dtos.append(dto)
            return Response(data=dtos, success=True, message="")
        except Exception as e:
            return Response(data=None, success=False,message=str(e))
    
    def add(self, item: UserEntity) -> Response:
        try:
            entity: DMLEntity = self.userRepository.add(item)
            return Response(success=True, message="Elemento registrado")

        except Exception as e:
            return Response(data=None, success=False,message=str(e))
        
    def update(self,item: UserEntity) ->Response:
        try:
            entity: DMLEntity = self.userRepository.update(item)
            return Response(success=True, message="Elemento Actualizado")
        
        except Exception as e:
            return Response(data=None, success=False, message=str(e))