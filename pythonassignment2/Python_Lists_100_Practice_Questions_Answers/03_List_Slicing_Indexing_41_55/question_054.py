# Python Lists – Practice Question 54
# Question: Rotate a list left by 2 positions using slicing.

numbers = [1, 2, 3, 4, 5]
k = 2
rotated = numbers[k:] + numbers[:k]
print(rotated)
