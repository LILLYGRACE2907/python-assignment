from abc import ABC, abstractmethod

class Delivery(ABC):

    @abstractmethod
    def calculate_charge(self):
        pass

    @abstractmethod
    def deliver(self):
        pass


class StandardDelivery(Delivery):

    def calculate_charge(self):
        print("Standard delivery charge: Rs. 50")

    def deliver(self):
        print("Delivered using Standard Delivery")


class ExpressDelivery(Delivery):

    def calculate_charge(self):
        print("Express delivery charge: Rs. 100")

    def deliver(self):
        print("Delivered using Express Delivery")


s = StandardDelivery()
s.calculate_charge()
s.deliver()

e = ExpressDelivery()
e.calculate_charge()
e.deliver()