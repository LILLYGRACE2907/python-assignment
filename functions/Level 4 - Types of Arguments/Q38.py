# Question 38
# Create a function that accepts any number of numbers using *args and returns the average.

def average(*args):
    return sum(args) / len(args)

print("Average =", average(10, 20, 30, 40))
