import json

student = {
    "id": 101,
    "name": "Lilly",
    "course": "Diploma CCN",
    "marks": 85
}

file = open("student.json", "w")

json.dump(student, file, indent=4)

file.close()

print("Dictionary converted to JSON")