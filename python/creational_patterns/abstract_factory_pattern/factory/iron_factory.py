from base_factory import BaseFactory
from ..products.chair.chair import Chair
from ..products.chair.iron_chair import IronChair
from ..products.table.table import Table
from ..products.table.iron_table import IronTable
from ..products.sofa.sofa import Sofa
from ..products.sofa.iron_sofa import IronSofa

# WoodFactory is a concrete class that defines the methods to create a chair, a table and a sofa made of wood.

class IronFactory(BaseFactory):

    def __init__(self):
        super().__init__()

    def createChair(self) -> Chair:
        print(f"Creating a iron chair..." )
        chair = IronChair()
        print(f"Chair created: {chair}, has legs: {chair.hasLegs()}, can sit on: {chair.sitOn()}")
        return chair


    def createTable(self) -> Table:
        print(f"Creating a iron table..." )
        table = IronTable()
        print(f"Table created: {table}, has legs: {table.hasLegs()}, shape: {table.shape()}")
        return table

    def createSofa(self) -> Sofa:
        print(f"Creating a iron sofa..." )
        sofa = IronSofa()
        print(f"Sofa created: {sofa}, confort level: {sofa.confortLevel()}, can sit on: {sofa.sitOn()}")
        return sofa