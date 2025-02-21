from abc import ABC, abstractmethod
from typing import List

from domain.entity.DMLEntity import DMLEntity
from domain.entity.UserEntity import UserEntity

class IUserRepository(ABC):
    @abstractmethod
    def findOne(self,id) -> UserEntity:
        return next((user for user in self.findAll() if user.id == id), None)
    def findAll(self) -> List[UserEntity]:
        return []
    def add(self,user: UserEntity) -> DMLEntity:
        self.users().append(user)
        return DMLEntity(True, "Usuario agregado")
    def update(self,item: UserEntity) -> DMLEntity:
        ...
    def updateEmail(self, id,email) -> DMLEntity:
        ...