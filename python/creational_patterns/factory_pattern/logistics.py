from abc import ABC, abstractmethod
from transport import Transport, Truck, Ship

# Defines an abstract class Logistics, that can plan deliveries by creating a Transport.
# The Logistics class is abstract, so it cannot be instantiated.
# The Logistics class has an abstract method createTransport, which must be implemented by subclasses.
# The behavior of the Logistics class is defined by the createTransport method, which is implemented by subclasses.
class Logistics(ABC):


    def __init__(self):
        pass

    def planDelivery(self):
        transport: Transport = self.createTransport()
        print(f'making delivery for transport: {transport.getTypeName()}...')
        transport.deliver()

    @abstractmethod
    def createTransport(self):
        pass

# Defines a subclass of Logistics, RoadLogistics, which implements the createTransport method for roadLogistics.
class RoadLogistics(Logistics):


    def __init__(self):
        super().__init__()

    def createTransport(self):
        return Truck()

# Defines a subclass of Logistics, RoadLogistics, which implements the createTransport method for roadLogistics.
class SeaLogistics(Logistics):

    def __init__(self):
        super().__init__()

    def createTransport(self):
        return Ship()


