class InvalidEnrollmentError(Exception):
    pass


class Course:
    def __init__(self, course_name, limit):
        self.course_name = course_name
        self.limit = limit
        self.students = []

    def enroll(self, student):
        try:
            if len(self.students) >= self.limit:
                raise InvalidEnrollmentError("Course is full")

            if student in self.students:
                raise InvalidEnrollmentError(
                    "Student is already enrolled"
                )

            self.students.append(student)

            print(student, "enrolled successfully")

        except InvalidEnrollmentError as e:
            print(e)


course = Course("Python", 2)

course.enroll("Lilly")
course.enroll("Ravi")
course.enroll("Anu")
course.enroll("Lilly")