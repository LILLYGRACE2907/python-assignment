marks = {
    "Lilly": 85,
    "Ravi": 70,
    "Anu": 95,
    "Priya": 60,
    "Kiran": 80
}

topper_name = None
topper_marks = None

lowest_name = None
lowest_marks = None

for name, mark in marks.items():

    if topper_marks is None or mark > topper_marks:
        topper_marks = mark
        topper_name = name

    if lowest_marks is None or mark < lowest_marks:
        lowest_marks = mark
        lowest_name = name

print("Topper:", topper_name, topper_marks)
print("Lowest scorer:", lowest_name, lowest_marks)