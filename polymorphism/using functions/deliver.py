class HomeDelivery:
    def deliver(self):
        print("Home delivery completed")


class StoreDelivery:
    def deliver(self):
        print("Store delivery completed")


class CourierDelivery:
    def deliver(self):
        print("Courier delivery completed")


def process_delivery(delivery):
    delivery.deliver()


home = HomeDelivery()
store = StoreDelivery()
courier = CourierDelivery()

process_delivery(home)
process_delivery(store)
process_delivery(courier)