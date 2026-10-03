# Python Lists – Practice Question 66
# Question: Replace negative numbers with 0.

numbers = [5, -2, 7, -4, 0]
result = [0 if n < 0 else n for n in numbers]
print(result)
