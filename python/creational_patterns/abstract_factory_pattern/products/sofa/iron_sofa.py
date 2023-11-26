from python.creational_patterns.abstract_factory_pattern.products.sofa.sofa import Sofa


class IronSofa(Sofa):

    def __init__(self):
        super().__init__()

    def confortLevel(self) -> int:
        return -5

    def sitOn(self) -> bool:
        return True

    def __str__(self) -> str:
        return "Iron Sofa"