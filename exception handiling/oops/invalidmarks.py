class InvalidMarksError(Exception):
    pass


class Student:
    def __init__(self, name):
        self.name = name

    def set_marks(self, marks):
        try:
            if marks < 0 or marks > 100:
                raise InvalidMarksError("Marks must be between 0 and 100")

            print("Marks:", marks)

        except InvalidMarksError as e:
            print(e)


student = Student("Lilly")

student.set_marks(85)
student.set_marks(120)