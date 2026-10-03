# Python Lists – Practice Question 40
# Question: Compare two lists and check whether they contain the same elements.

list1 = [1, 2, 3, 4]
list2 = [4, 3, 2, 1]
if sorted(list1) == sorted(list2):
    print("Same elements")
else:
    print("Different elements")
