class InvalidSalaryError(Exception):
    pass


try:
    salary = float(input("Enter salary: "))

    if salary < 0:
        raise InvalidSalaryError("Salary cannot be negative")

    print("Valid salary")

except InvalidSalaryError as e:
    print(e)