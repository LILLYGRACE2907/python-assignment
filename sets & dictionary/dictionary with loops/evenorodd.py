numbers = {
    "a": 10,
    "b": 15,
    "c": 20,
    "d": 25,
    "e": 30
}

even_count = 0
odd_count = 0

for value in numbers.values():
    if value % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)