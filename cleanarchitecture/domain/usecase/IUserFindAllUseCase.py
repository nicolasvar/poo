from abc import ABC, abstractmethod

from domain.valueobject.Response import Response
from application.dto.UserFindAllResponse import UserFindAllResponse

class IUserFindAllUseCase(ABC):
    @abstractmethod
    def findAll(self) -> Response:
        ...