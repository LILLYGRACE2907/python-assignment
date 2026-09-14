#intersection
students1 = {"Lilly", "Ravi", "Anu", "Priya"}
students2 = {"Anu", "Priya", "Kiran", "Rahul"}

common = students1.intersection(students2)

print("Students present in both:", common)


#difference
students1 = {"Lilly", "Ravi", "Anu", "Priya"}
students2 = {"Anu", "Priya", "Kiran", "Rahul"}

only_first = students1.difference(students2)

print("Students only in first set:", only_first)

#union
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

unique = set1.union(set2)

print("Unique numbers:", unique)