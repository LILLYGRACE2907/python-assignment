import json

student = {
    "id": 101,
    "name": "Rahul",
    "course": "Python",
    "marks": 85
}

file = open("student.json", "w")

json.dump(student, file, indent=4)

file.close()