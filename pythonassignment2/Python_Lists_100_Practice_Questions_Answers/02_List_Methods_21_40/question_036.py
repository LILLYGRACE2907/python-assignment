# Python Lists – Practice Question 36
# Question: Remove all occurrences of a particular number.

numbers = [2, 4, 2, 6, 2, 8]
target = 2
numbers = [n for n in numbers if n != target]
print(numbers)
