from abc import ABC, abstractmethod


class Delivery(ABC):

    @abstractmethod
    def calculate_delivery_charge(self):
        pass


class LocalDelivery(Delivery):
    def calculate_delivery_charge(self):
        print("Local Delivery Charge: 50")


class ExpressDelivery(Delivery):
    def calculate_delivery_charge(self):
        print("Express Delivery Charge: 100")


class InternationalDelivery(Delivery):
    def calculate_delivery_charge(self):
        print("International Delivery Charge: 500")


local = LocalDelivery()
express = ExpressDelivery()
international = InternationalDelivery()

local.calculate_delivery_charge()
express.calculate_delivery_charge()
international.calculate_delivery_charge()