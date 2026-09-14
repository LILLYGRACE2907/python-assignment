# Question 62
# Create a Student Marks Management System using Functions with options to add, search, update, delete, and display students.

students = {}

def add_student():
    name = input("Name: ")
    marks = float(input("Marks: "))
    students[name] = marks

def search_student():
    name = input("Name: ")
    print(students.get(name, "Student not found"))

def update_student():
    name = input("Name: ")
    if name in students:
        students[name] = float(input("New marks: "))
    else:
        print("Student not found")

def delete_student():
    name = input("Name: ")
    if name in students:
        del students[name]
    else:
        print("Student not found")

def display_students():
    for name, marks in students.items():
        print(name, ":", marks)

while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit")
    choice = input("Choice: ")
    if choice == "1": add_student()
    elif choice == "2": search_student()
    elif choice == "3": update_student()
    elif choice == "4": delete_student()
    elif choice == "5": display_students()
    elif choice == "6": break
    else: print("Invalid choice")
