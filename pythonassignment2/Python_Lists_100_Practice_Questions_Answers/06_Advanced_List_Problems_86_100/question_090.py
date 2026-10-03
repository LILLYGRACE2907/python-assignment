# Python Lists – Practice Question 90
# Question: Move all negative numbers to the beginning of a list.

numbers = [3, -2, 5, -7, 8, -1]
negative = [n for n in numbers if n < 0]
positive = [n for n in numbers if n >= 0]
print(negative + positive)
