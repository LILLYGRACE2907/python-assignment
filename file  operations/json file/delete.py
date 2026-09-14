import json

file = open("students.json", "r")
students = json.load(file)
file.close()

students = [s for s in students if s["id"] != 101]

file = open("students.json", "w")
json.dump(students, file, indent=4)
file.close()