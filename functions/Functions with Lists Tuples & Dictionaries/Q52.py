# Question 52
# Create a function that accepts a tuple and returns the sum of all its elements.

def tuple_sum(values):
    total = 0
    for value in values:
        total += value
    return total

print("Sum =", tuple_sum((10, 20, 30)))
