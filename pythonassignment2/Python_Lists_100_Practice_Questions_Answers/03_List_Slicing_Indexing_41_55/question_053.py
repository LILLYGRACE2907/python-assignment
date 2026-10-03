# Python Lists – Practice Question 53
# Question: Split a list into two equal halves.

numbers = [1, 2, 3, 4, 5, 6]
mid = len(numbers) // 2
first = numbers[:mid]
second = numbers[mid:]
print(first)
print(second)
