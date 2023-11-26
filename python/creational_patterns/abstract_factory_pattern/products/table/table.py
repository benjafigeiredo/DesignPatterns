from abc import ABC, abstractmethod

class Table(ABC):

        def __init__(self):
            pass

        @abstractmethod
        def hasLegs(self) -> bool:
            pass

        @abstractmethod
        def shape(self) -> str:
            pass

        @abstractmethod
        def __str__(self) -> str:
            pass