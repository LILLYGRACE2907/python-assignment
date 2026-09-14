class Manager:
    def work(self):
        print("Manager is managing the team")


class Developer:
    def work(self):
        print("Developer is writing code")


class Tester:
    def work(self):
        print("Tester is testing software")


def assign_work(employee):
    employee.work()


manager = Manager()
developer = Developer()
tester = Tester()

assign_work(manager)
assign_work(developer)
assign_work(tester)