def search_key(student, key):
    try:
        return student[key]

    except KeyError:
        return "Key not found"


student = {
    "name": "Lilly",
    "age": 18,
    "course": "CCN"
}

key = input("Enter key: ")

print("Value:", search_key(student, key))