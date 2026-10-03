# Python Lists – Practice Question 55
# Question: Rotate a list right by 3 positions using slicing.

numbers = [1, 2, 3, 4, 5, 6]
k = 3
rotated = numbers[-k:] + numbers[:-k]
print(rotated)
