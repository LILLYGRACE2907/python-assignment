#max()
numbers = {10, 50, 30, 80, 20}

smallest = None

for num in numbers:
    if smallest is None or num < smallest:
        smallest = num

print("Smallest number:", smallest)

#min()
numbers = {10, 50, 30, 80, 20}

smallest = None

for num in numbers:
    if smallest is None or num < smallest:
        smallest = num

print("Smallest number:", smallest)


#remove duplicates
students = ["Lilly", "Ravi", "Lilly", "Anu", "Ravi", "Priya"]

unique_students = set(students)

print("Unique students:", uniqude_students)


#python and java
python_students = {"Lilly", "Ravi", "Anu", "Priya"}
java_students = {"Anu", "Priya", "Kiran", "Rahul"}

both = python_students.intersection(java_students)

print("Students enrolled in both:", both)

#symmertic difference
event1 = {"Lilly", "Ravi", "Anu", "Priya"}
event2 = {"Anu", "Priya", "Kiran", "Rahul"}

one_event = event1.symmetric_difference(event2)

print("Students who attended exactly one event:", one_event)