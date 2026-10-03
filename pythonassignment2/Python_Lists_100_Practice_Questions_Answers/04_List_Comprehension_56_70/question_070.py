# Python Lists – Practice Question 70
# Question: Create a list of numbers whose square is greater than 100.

numbers = range(1, 21)
result = [n for n in numbers if n * n > 100]
print(result)
