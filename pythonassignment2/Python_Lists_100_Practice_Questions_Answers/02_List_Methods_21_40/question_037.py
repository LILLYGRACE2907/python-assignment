# Python Lists – Practice Question 37
# Question: Replace all occurrences of one value with another.

numbers = [1, 2, 3, 2, 4, 2]
old = 2
new = 9
numbers = [new if n == old else n for n in numbers]
print(numbers)
