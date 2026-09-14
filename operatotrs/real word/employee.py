salary = float(input("Enter basic salary: "))
increment = float(input("Enter increment percentage: "))

increase = salary * increment / 100
salary += increase

print("Final Salary =", salary)