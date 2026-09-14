# Question 54
# Create a function that accepts a dictionary of student marks and returns the topper's name.

def topper(marks):
    topper_name = None
    highest = -1
    for name, mark in marks.items():
        if mark > highest:
            highest = mark
            topper_name = name
    return topper_name

students = {"Lilly": 85, "Anu": 92, "Ravi": 78}
print("Topper =", topper(students))
