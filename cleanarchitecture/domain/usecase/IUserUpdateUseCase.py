from abc import ABC, abstractmethod

from domain.valueobject.Response import Response
from domain.entity.UserEntity import UserEntity

class IUserUpdateUseCase(ABC):
    @abstractmethod
    def update(self, item: UserEntity) -> Response:
        ...