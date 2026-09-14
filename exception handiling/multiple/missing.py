student = {
    "name": "Lilly",
    "age": 18,
    "course": "CCN"
}

try:
    key = input("Enter key: ")

    if key == "":
        raise ValueError("Key cannot be empty")

    print("Value:", student[key])

except ValueError as e:
    print(e)

except KeyError:
    print("Key not found")

except TypeError:
    print("Invalid key type")