keys = ["name", "age", "course", "marks"]

values = ["Lilly", 18, "CCN", 85]

student = {}

for i in range(len(keys)):
    student[keys[i]] = values[i]

print(student)