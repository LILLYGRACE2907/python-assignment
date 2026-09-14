salaries = {
    "Lilly": 30000,
    "Ravi": 40000,
    "Anu": 35000,
    "Priya": 45000
}

total = 0

for salary in salaries.values():
    total = total + salary

average = total / len(salaries)

print("Average salary:", average)