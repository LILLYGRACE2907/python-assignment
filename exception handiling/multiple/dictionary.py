student = {
    "name": "Lilly",
    "age": 18,
    "course": "CCN"
}

try:
    key = input("Enter key: ")
    print("Value:", student[key])

except KeyError:
    print("Key does not exist")

except TypeError:
    print("Invalid key type")