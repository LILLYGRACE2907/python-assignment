class InvalidEmployeeIDError(Exception):
    pass


class InvalidSalaryError(Exception):
    pass


class InvalidDepartmentError(Exception):
    pass


class Employee:
    def __init__(self, emp_id, name, department, salary):

        if emp_id <= 0:
            raise InvalidEmployeeIDError("Invalid employee ID")

        if salary < 0:
            raise InvalidSalaryError("Salary cannot be negative")

        departments = ["HR", "IT", "Sales"]

        if department not in departments:
            raise InvalidDepartmentError("Invalid department")

        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary


try:
    employee = Employee(
        101,
        "Lilly",
        "IT",
        30000
    )

    print("Employee created")
    print(employee.name)

except InvalidEmployeeIDError as e:
    print(e)

except InvalidSalaryError as e:
    print(e)

except InvalidDepartmentError as e:
    print(e)