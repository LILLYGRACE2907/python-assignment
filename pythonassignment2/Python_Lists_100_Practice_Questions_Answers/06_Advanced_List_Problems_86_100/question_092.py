# Python Lists – Practice Question 92
# Question: Rotate a list by K positions.

numbers = [1, 2, 3, 4, 5, 6]
k = 2
k = k % len(numbers)
rotated = numbers[-k:] + numbers[:-k]
print(rotated)
