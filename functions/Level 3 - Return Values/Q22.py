# Question 22
# Create a function that accepts a student's marks and returns their grade.

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    return "F"

print("Grade =", grade(82))
