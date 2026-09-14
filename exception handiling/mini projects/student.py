class InvalidMarksError(Exception):
    pass


class DuplicateStudentError(Exception):
    pass


class StudentNotFoundError(Exception):
    pass


class Student:
    def __init__(self, student_id, name, marks):
        if marks < 0 or marks > 100:
            raise InvalidMarksError("Marks must be between 0 and 100")

        self.student_id = student_id
        self.name = name
        self.marks = marks


students = []


def add_student(student_id, name, marks):
    for student in students:
        if student.student_id == student_id:
            raise DuplicateStudentError("Student ID already exists")

    student = Student(student_id, name, marks)
    students.append(student)

    print("Student added")


def search_student(student_id):
    for student in students:
        if student.student_id == student_id:
            print("Name:", student.name)
            print("Marks:", student.marks)
            return

    raise StudentNotFoundError("Student not found")


try:
    add_student(1, "Lilly", 85)
    add_student(2, "Ravi", 90)

    search_student(1)

except InvalidMarksError as e:
    print(e)

except DuplicateStudentError as e:
    print(e)

except StudentNotFoundError as e:
    print(e)