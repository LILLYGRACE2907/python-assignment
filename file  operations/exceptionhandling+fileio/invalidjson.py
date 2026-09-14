import json

try:
    file = open("student.json", "r")
    data = json.load(file)

    print(data)

    file.close()

except json.JSONDecodeError:
    print("Invalid JSON data") 