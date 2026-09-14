class Developer:
    def work(self):
        print("Developer writes code")


class Tester:
    def work(self):
        print("Tester tests the software")


class Manager:
    def work(self):
        print("Manager manages the team")


employees = [Developer(), Tester(), Manager()]

for employee in employees:
    employee.work()