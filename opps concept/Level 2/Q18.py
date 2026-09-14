# Question 18
# Create a Company class that HAS-A multiple Department objects.

class Department:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self):
        self.departments = []

    def add_department(self, obj):
        self.departments.append(obj)

    def show_departments(self):
        print("Company contains:", [x.name for x in self.departments])

obj = Company()
obj.add_department(Department("Example 1"))
obj.add_department(Department("Example 2"))
obj.show_departments()
