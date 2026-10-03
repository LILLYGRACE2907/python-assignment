# Python Lists – Practice Question 77
# Question: Find the intersection of three lists.

list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5]
list3 = [3, 4, 5, 6]
result = [n for n in list1 if n in list2 and n in list3]
print(result)
