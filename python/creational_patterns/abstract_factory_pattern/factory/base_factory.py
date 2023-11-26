from abc import ABC, abstractmethod
from python.creational_patterns.abstract_factory_pattern.products.chair.chair import Chair
from python.creational_patterns.abstract_factory_pattern.products.table.table import Table
from python.creational_patterns.abstract_factory_pattern.products.sofa.sofa import Sofa

# BaseFactory is an abstract class which declares the methods to create a chair, a table and a sofa.
class BaseFactory(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def createChair(self) -> Chair:
        pass

    @abstractmethod
    def createTable(self) -> Table:
        pass

    def createSofa(self) -> Sofa:
        pass