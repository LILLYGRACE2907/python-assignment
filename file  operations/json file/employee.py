import json

employees = [
    {"id": 1, "name": "Rahul", "salary": 30000},
    {"id": 2, "name": "Priya", "salary": 40000},
    {"id": 3, "name": "Kiran", "salary": 35000}
]

file = open("employees.json", "w")

json.dump(employees, file, indent=4)

file.close()