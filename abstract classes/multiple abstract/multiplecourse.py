from abc import ABC, abstractmethod

class Course(ABC):

    @abstractmethod
    def start_course(self):
        pass

    @abstractmethod
    def get_duration(self):
        pass


class OnlineCourse(Course):

    def start_course(self):
        print("Online course started")

    def get_duration(self):
        print("Duration: 3 months")


class OfflineCourse(Course):

    def start_course(self):
        print("Offline course started")

    def get_duration(self):
        print("Duration: 6 months")


o = OnlineCourse()
o.start_course()
o.get_duration()

f = OfflineCourse()
f.start_course()
f.get_duration()