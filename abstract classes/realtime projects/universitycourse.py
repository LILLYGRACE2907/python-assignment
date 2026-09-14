from abc import ABC, abstractmethod

class UniversityCourse(ABC):

    @abstractmethod
    def study(self):
        pass


class Engineering(UniversityCourse):

    def study(self):
        print("Engineering course")


class Medical(UniversityCourse):

    def study(self):
        print("Medical course")


class Management(UniversityCourse):

    def study(self):
        print("Management course")


Engineering().study()
Medical().study()
Management().study()