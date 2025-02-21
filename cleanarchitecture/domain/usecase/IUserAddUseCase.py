from abc import ABC, abstractmethod

from domain.valueobject.Response import Response
from domain.entity.UserEntity import UserEntity

class IUserAddUseCase(ABC):
    @abstractmethod
    def add(self, item: UserEntity) -> Response:
        ...