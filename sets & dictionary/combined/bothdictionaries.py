python_marks = {
    "Lilly": 85,
    "Ravi": 75,
    "Anu": 90,
    "Priya": 80
}

java_marks = {
    "Anu": 88,
    "Priya": 85,
    "Kiran": 70,
    "Rahul": 78
}

students1 = set(python_marks.keys())
students2 = set(java_marks.keys())

common = students1.intersection(students2)

print("Students in both subjects:", common)