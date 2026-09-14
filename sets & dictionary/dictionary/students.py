marks = {
    "Lilly": 85,
    "Ravi": 75,
    "Anu": 95,
    "Priya": 80
}

highest_name = None
highest_marks = None

for name, mark in marks.items():

    if highest_marks is None or mark > highest_marks:
        highest_marks = mark
        highest_name = name

print("Highest marks:", highest_name)
print("Marks:", highest_marks)