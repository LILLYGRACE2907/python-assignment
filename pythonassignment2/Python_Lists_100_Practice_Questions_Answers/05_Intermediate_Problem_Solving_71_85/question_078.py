# Python Lists – Practice Question 78
# Question: Find the union of two lists without using set().

list1 = [1, 2, 3]
list2 = [3, 4, 5]
union = []
for n in list1 + list2:
    if n not in union:
        union.append(n)
print(union)
