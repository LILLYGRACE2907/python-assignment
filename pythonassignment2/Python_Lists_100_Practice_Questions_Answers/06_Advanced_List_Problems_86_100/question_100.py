# Python Lists – Practice Question 100
# Question: Mini Project: Given a list of student records containing name, marks, and course, find topper, class average, students above 80, lowest scorer, rank students, duplicate records, group by course, highest scorer in each course, and final Pass/Fail/Distinction result.

students = [
    {"name": "Anu", "marks": 92, "course": "Python"},
    {"name": "Ravi", "marks": 78, "course": "Python"},
    {"name": "Sita", "marks": 88, "course": "Java"},
    {"name": "Kiran", "marks": 65, "course": "Java"},
    {"name": "Anu", "marks": 92, "course": "Python"},
]

# Topper
topper = max(students, key=lambda s: s["marks"])
print("Topper:", topper)

# Class average
average = sum(s["marks"] for s in students) / len(students)
print("Class average:", average)

# Above 80
above_80 = [s for s in students if s["marks"] > 80]
print("Above 80:", above_80)

# Lowest scorer
lowest = min(students, key=lambda s: s["marks"])
print("Lowest scorer:", lowest)

# Rank students by marks
ranked = sorted(students, key=lambda s: s["marks"], reverse=True)
for rank, student in enumerate(ranked, start=1):
    print(rank, student["name"], student["marks"])

# Duplicate records
duplicates = []
for student in students:
    if students.count(student) > 1 and student not in duplicates:
        duplicates.append(student)
print("Duplicate records:", duplicates)

# Group students by course
groups = {}
for student in students:
    groups.setdefault(student["course"], []).append(student)
print("Groups:", groups)

# Highest scorer in each course
for course, group in groups.items():
    highest = max(group, key=lambda s: s["marks"])
    print("Highest in", course, ":", highest)

# Final result
for student in students:
    if student["marks"] >= 75:
        result = "Distinction"
    elif student["marks"] >= 40:
        result = "Pass"
    else:
        result = "Fail"
    print(student["name"], result)
