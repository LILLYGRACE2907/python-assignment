# Python Lists – Practice Question 17
# Question: Find the second-largest number in a list.

numbers = [10, 50, 30, 40, 20]
unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)
unique.sort()
print("Second largest:", unique[-2])
