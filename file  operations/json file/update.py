import json

file = open("students.json", "r")
students = json.load(file)
file.close()

for student in students:
    if student["id"] == 101:
        student["marks"] = 95

file = open("students.json", "w")
json.dump(students, file, indent=4)
file.close()