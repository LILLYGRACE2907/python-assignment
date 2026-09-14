import json

file = open("student.json", "r")

student = json.load(file)

print(student)

file.close()