class Student:

    def grade(self, marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "Fail"


s = Student()

result = s.grade(85)

print("Grade:", result)