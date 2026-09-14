# Question 23
# Create a function that accepts a list of numbers and returns the average.

def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

print("Average =", average([10, 20, 30, 40]))
