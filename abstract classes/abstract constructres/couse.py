from abc import ABC, abstractmethod

class Course(ABC):

    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def start_course(self):
        pass


class OnlineCourse(Course):

    def start_course(self):
        print("Online course started")


class OfflineCourse(Course):

    def start_course(self):
        print("Offline course started")


o = OnlineCourse("Python", "3 Months")
f = OfflineCourse("Java", "6 Months")

print("Course:", o.course_name)
print("Duration:", o.duration)
o.start_course()

print("Course:", f.course_name)
print("Duration:", f.duration)
f.start_course()