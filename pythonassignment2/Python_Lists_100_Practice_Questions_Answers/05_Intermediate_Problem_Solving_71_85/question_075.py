# Python Lists – Practice Question 75
# Question: Find elements present in the first list but not the second.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 6]
result = [n for n in list1 if n not in list2]
print(result)
