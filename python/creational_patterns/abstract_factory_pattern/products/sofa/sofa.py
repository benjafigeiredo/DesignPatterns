from abc import ABC, abstractmethod

class Sofa(ABC):

        def __init__(self):
            pass

        @abstractmethod
        def confortLevel(self) -> int:
            pass

        @abstractmethod
        def sitOn(self) -> bool:
            pass

        @abstractmethod
        def __str__(self) -> str:
            pass