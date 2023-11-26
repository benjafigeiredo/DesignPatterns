from python.creational_patterns.abstract_factory_pattern.factory.base_factory import BaseFactory
from python.creational_patterns.abstract_factory_pattern.factory.wood_factory import WoodFactory
from python.creational_patterns.abstract_factory_pattern.factory.iron_factory import IronFactory
from python.creational_patterns.abstract_factory_pattern.client.client import Client


if __name__ == "__main__":
    wood_factory: BaseFactory = WoodFactory()
    client: Client = Client(wood_factory)
    print("creating products with wood factory...")
    chair, sofa, table = client.createProducts()
    print(f"Chair: {chair}, Table: {table}, Sofa: {sofa}")

    iron_factory: BaseFactory = IronFactory()
    client.setFactory(iron_factory)
    print("creating products with iron factory...")
    chair, sofa, table = client.createProducts()
    print(f"Chair: {chair}, Table: {table}, Sofa: {sofa}")
