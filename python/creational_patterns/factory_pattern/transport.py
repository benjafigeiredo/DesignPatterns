from abc import ABC, abstractmethod

# Defines an "interface" for creating objects, but let subclasses decide which class to instantiate
class Transport(ABC):
    @abstractmethod
    def getTypeName(self):
        pass

    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def getTypeName(self):
        return 'Truck'

    def deliver(self):
        print('delivering by truck...')

class Ship(Transport):
    def getTypeName(self):
        return 'Ship'

    def deliver(self):
        print('delivering by ship...')