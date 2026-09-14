# Question 63
# Create an Employee Management System using Functions with options to add, search, update, delete, and display employees.

employees = {}

def add_employee():
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    employees[emp_id] = name

def search_employee():
    emp_id = input("Employee ID: ")
    print(employees.get(emp_id, "Employee not found"))

def update_employee():
    emp_id = input("Employee ID: ")
    if emp_id in employees:
        employees[emp_id] = input("New name: ")
    else:
        print("Employee not found")

def delete_employee():
    emp_id = input("Employee ID: ")
    if emp_id in employees:
        del employees[emp_id]

def display_employees():
    for emp_id, name in employees.items():
        print(emp_id, ":", name)

while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit")
    choice = input("Choice: ")
    if choice == "1": add_employee()
    elif choice == "2": search_employee()
    elif choice == "3": update_employee()
    elif choice == "4": delete_employee()
    elif choice == "5": display_employees()
    elif choice == "6": break
    else: print("Invalid choice")
