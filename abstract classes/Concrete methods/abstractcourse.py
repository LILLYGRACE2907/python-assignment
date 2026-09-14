from abc import ABC, abstractmethod

class Course(ABC):

    @abstractmethod
    def start(self):
        pass

    def display_course_details(self):
        print("Course: Python")


class PythonCourse(Course):

    def start(self):
        print("Python course started")


c = PythonCourse()
c.start()
c.display_course_details()