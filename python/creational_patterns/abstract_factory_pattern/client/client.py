from python.creational_patterns.abstract_factory_pattern.factory.base_factory import BaseFactory

class Client:

    def __init__(self, factory: BaseFactory):
        self.factory = factory

    def createProducts(self):
        return self.factory.createChair(), self.factory.createTable(), self.factory.createSofa()

    def setFactory(self, factory: BaseFactory):
        self.factory = factory
