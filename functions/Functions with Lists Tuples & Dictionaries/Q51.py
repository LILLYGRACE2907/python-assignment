# Question 51
# Create a function that accepts a list of numbers and returns a tuple containing the minimum and maximum values.

def min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return (minimum, maximum)

print(min_max([10, 5, 30, 2, 20]))
