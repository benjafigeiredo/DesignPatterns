from base_factory import BaseFactory
from ..products.chair.chair import Chair
from ..products.chair.wood_chair import WoodChair
from ..products.table.table import Table
from ..products.table.wood_table import WoodTable
from ..products.sofa.sofa import Sofa
from ..products.sofa.wood_sofa import WoodSofa

# WoodFactory is a concrete class that defines the methods to create a chair, a table and a sofa made of wood.

class WoodFactory(BaseFactory):

    def __init__(self):
        super().__init__()

    def createChair(self) -> Chair:
        print(f"Creating a wood chair..." )
        chair = WoodChair()
        print(f"Chair created: {chair}, has legs: {chair.hasLegs()}, can sit on: {chair.sitOn()}")
        return chair


    def createTable(self) -> Table:
        print(f"Creating a wood table..." )
        table = WoodTable()
        print(f"Table created: {table}, has legs: {table.hasLegs()}, shape: {table.shape()}")
        return table

    def createSofa(self) -> Sofa:
        print(f"Creating a wood sofa..." )
        sofa = WoodSofa()
        print(f"Sofa created: {sofa}, confort level: {sofa.confortLevel()}, can sit on: {sofa.sitOn()}")
        return sofa