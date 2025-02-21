from pydantic import BaseModel
from adapter.dto.UserAddRequest import UserAddRequest
from adapter.dto.UserUpdateRequest import UserUpdateRequest
from domain.entity.UserEntity import UserEntity


class UserMaper:
    @staticmethod
    def toAddEntity(dto: UserAddRequest) -> UserEntity:
        entity = UserEntity()
        entity.id = dto.id
        entity.name = dto.username
        entity.email = dto.email
        return entity
    
    @staticmethod
    def toUpdateEntity(dto: UserUpdateRequest) -> UserEntity:
        entity = UserEntity()
        entity.id = dto.id
        entity.name = dto.name
        entity.email = dto.email
        return entity