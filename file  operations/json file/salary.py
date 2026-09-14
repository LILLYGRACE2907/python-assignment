import json

file = open("employees.json", "r")

employees = json.load(file)

highest = max(employees, key=lambda x: x["salary"])

print("Highest Salary Employee:")
print(highest)

file.close()