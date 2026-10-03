# Python Lists – Practice Question 73
# Question: Find all unique elements in a list.

numbers = [1, 2, 2, 3, 4, 4, 5]
unique = []
for n in numbers:
    if numbers.count(n) == 1:
        unique.append(n)
print(unique)
