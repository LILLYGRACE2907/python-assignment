class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def display_students(self):
        print("Course:", self.course_name)

        for student in self.students:
            print(student)


c = Course("Python")

c.add_student("Lilly")
c.add_student("Anu")
c.add_student("Ravi")

c.display_students()