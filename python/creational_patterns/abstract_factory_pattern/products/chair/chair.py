from abc import ABC, abstractmethod

class Chair(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def hasLegs(self) -> bool:
        pass

    @abstractmethod
    def sitOn(self) -> bool:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass