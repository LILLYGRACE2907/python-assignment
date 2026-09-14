# Question 35
# Create a function using *args to find the largest number from any number of arguments.

def largest(*args):
    largest_value = args[0]
    for n in args:
        if n > largest_value:
            largest_value = n
    return largest_value

print("Largest =", largest(10, 50, 20, 40))
