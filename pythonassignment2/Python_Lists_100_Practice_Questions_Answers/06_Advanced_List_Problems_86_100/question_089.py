# Python Lists – Practice Question 89
# Question: Move all zeros to the end of a list while maintaining the order of other elements.

numbers = [0, 1, 0, 3, 12]
result = [n for n in numbers if n != 0]
result.extend([0] * numbers.count(0))
print(result)
