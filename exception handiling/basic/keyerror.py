try:
    student = {
        "name": "Lilly",
        "age": 18
    }

    print(student["course"])

except KeyError:
    print("Key does not exist")