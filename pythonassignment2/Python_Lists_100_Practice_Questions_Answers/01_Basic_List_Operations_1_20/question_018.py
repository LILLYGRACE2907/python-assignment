# Python Lists – Practice Question 18
# Question: Find the second-smallest number in a list.

numbers = [10, 50, 30, 40, 20]
unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)
unique.sort()
print("Second smallest:", unique[1])
