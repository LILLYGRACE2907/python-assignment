# Python Lists – Practice Question 14
# Question: Create a new list containing cubes of all numbers.

numbers = [1, 2, 3, 4, 5]
cubes = []
for n in numbers:
    cubes.append(n ** 3)
print(cubes)
