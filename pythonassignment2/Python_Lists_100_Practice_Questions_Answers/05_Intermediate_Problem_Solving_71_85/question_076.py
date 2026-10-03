# Python Lists – Practice Question 76
# Question: Merge two lists and remove duplicates.

list1 = [1, 2, 3]
list2 = [3, 4, 5]
merged = []
for n in list1 + list2:
    if n not in merged:
        merged.append(n)
print(merged)
