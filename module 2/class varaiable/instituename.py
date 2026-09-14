class Course:
    institute_name = "ABC Institute"

    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    def display(self):
        print("Institute:", Course.institute_name)
        print("Course:", self.course_name)
        print("Duration:", self.duration)
        print()


c1 = Course("Python", "3 Months")
c2 = Course("Java", "4 Months")
c3 = Course("Web Development", "6 Months")

c1.display()
c2.display()
c3.display()