from abc import ABC, abstractmethod

class HospitalEmployee(ABC):

    @abstractmethod
    def work(self):
        pass


class Doctor(HospitalEmployee):

    def work(self):
        print("Doctor treats patients")


class Nurse(HospitalEmployee):

    def work(self):
        print("Nurse takes care of patients")


class Pharmacist(HospitalEmployee):

    def work(self):
        print("Pharmacist provides medicines")


Doctor().work()
Nurse().work()
Pharmacist().work()