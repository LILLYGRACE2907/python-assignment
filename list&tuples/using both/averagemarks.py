students = [
    ["Lilly", 80, 85, 90],
    ["Ravi", 70, 75, 80],
    ["Anu", 90, 95, 85]
]

for student in students:
    name = student[0]

    total = student[1] + student[2] + student[3]
    average = total / 3

    print("Name:", name)
    print("Total:", total)
    print("Average:", average)
    print()