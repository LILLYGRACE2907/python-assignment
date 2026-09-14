class SalesReport:
    def generate(self):
        print("Sales report generated")


class StudentReport:
    def generate(self):
        print("Student report generated")


class EmployeeReport:
    def generate(self):
        print("Employee report generated")


def generate_report(report):
    report.generate()


sales = SalesReport()
student = StudentReport()
employee = EmployeeReport()

generate_report(sales)
generate_report(student)
generate_report(employee)