from logistics import Logistics, RoadLogistics, SeaLogistics

def main():
    roadLogistics: Logistics = RoadLogistics()
    roadLogistics.planDelivery()

    seaLogistics: Logistics = SeaLogistics()
    seaLogistics.planDelivery()

if __name__ == '__main__':
    main()