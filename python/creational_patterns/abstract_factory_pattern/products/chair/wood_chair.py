from python.creational_patterns.abstract_factory_pattern.products.chair.chair import Chair


class WoodChair(Chair):

        def __init__(self):
            super().__init__()

        def hasLegs(self) -> bool:
            return True

        def sitOn(self) -> bool:
            return True

        def __str__(self) -> str:
            return "Wood Chair"