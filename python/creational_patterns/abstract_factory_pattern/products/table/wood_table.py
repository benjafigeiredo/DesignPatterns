from python.creational_patterns.abstract_factory_pattern.products.table.table import Table

# WoodTable is a concrete class that implements the abstract class Table.
class WoodTable(Table):

        def __init__(self):
            super().__init__()

        def hasLegs(self) -> bool:
            return True

        def shape(self) -> str:
            return "square"

        def __str__(self) -> str:
            return "Wood Table"