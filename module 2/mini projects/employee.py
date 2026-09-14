class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(self.emp_id, self.name, self.department, self.salary)


employees = []


def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    employee = Employee(emp_id, name, department, salary)
    employees.append(employee)

    print("Employee added")


def search_employee():
    emp_id = int(input("Enter Employee ID: "))

    for employee in employees:
        if employee.emp_id == emp_id:
            employee.display()
            return

    print("Employee not found")


def display_employees():
    for employee in employees:
        employee.display()


while True:
    print("\n1. Add Employee")
    print("2. Search Employee")
    print("3. Display Employees")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_employee()
    elif choice == 2:
        search_employee()
    elif choice == 3:
        display_employees()
    elif choice == 4:
        break
    else:
        print("Invalid choice")