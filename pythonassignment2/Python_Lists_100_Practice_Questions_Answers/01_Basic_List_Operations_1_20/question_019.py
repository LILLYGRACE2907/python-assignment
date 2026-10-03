# Python Lists – Practice Question 19
# Question: Swap the first and last elements of a list.

numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)
