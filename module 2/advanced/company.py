class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, name):
        self.employees.append(name)

    def remove_employee(self, name):
        if name in self.employees:
            self.employees.remove(name)
            print("Employee removed")
        else:
            print("Employee not found")

    def search_employee(self, name):
        if name in self.employees:
            print("Employee found")
        else:
            print("Employee not found")

    def display_employees(self):
        for employee in self.employees:
            print(employee)


c = Company()

c.add_employee("Ravi")
c.add_employee("Anu")
c.add_employee("Kiran")

c.search_employee("Anu")

c.remove_employee("Kiran")

c.display_employees()