employees = {
    "Lilly": 45000,
    "Ravi": 60000,
    "Anu": 55000,
    "Priya": 40000,
    "Kiran": 70000
}

for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)