students = [
    "Lilly",
    "Ravi",
    "Lilly",
    "Anu",
    "Ravi",
    "Lilly"
]

frequency = {}

for name in students:
    if name in frequency:
        frequency[name] += 1
    else:
        frequency[name] = 1

print(frequency)