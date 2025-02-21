from abc import ABC, abstractmethod

from application.dto.UserFindOneResponse import UserFindOneResponse

class IUserFindOneUseCase(ABC):
    @abstractmethod
    def findOne(self, id:int) -> UserFindOneResponse:
        ...