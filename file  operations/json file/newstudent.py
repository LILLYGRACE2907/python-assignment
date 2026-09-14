import json

file = open("students.json", "r")
students = json.load(file)
file.close()

new_student = {
    "id": 103,
    "name": "Anjali",
    "marks": 78
}

students.append(new_student)

file = open("students.json", "w")
json.dump(students, file, indent=4)
file.close()