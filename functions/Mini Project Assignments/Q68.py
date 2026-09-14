# Question 68
# Create a Student Grade Management System using Functions that calculates total, average, grade, pass/fail status, and topper.

students = {}

def add_student():
    name = input("Name: ")
    marks = [float(input("Mark 1: ")), float(input("Mark 2: ")), float(input("Mark 3: "))]
    students[name] = marks

def calculate(marks):
    total = sum(marks)
    average = total / len(marks)
    if average >= 90: grade = "A"
    elif average >= 75: grade = "B"
    elif average >= 60: grade = "C"
    elif average >= 40: grade = "D"
    else: grade = "F"
    return total, average, grade

def display():
    for name, marks in students.items():
        total, average, grade = calculate(marks)
        status = "Pass" if average >= 40 else "Fail"
        print(name, "Total:", total, "Average:", average, "Grade:", grade, status)

def topper():
    if students:
        name = max(students, key=lambda x: sum(students[x]))
        print("Topper:", name)

while True:
    print("\n1.Add Student 2.Display 3.Topper 4.Exit")
    choice = input("Choice: ")
    if choice == "1": add_student()
    elif choice == "2": display()
    elif choice == "3": topper()
    elif choice == "4": break
    else: print("Invalid choice")
