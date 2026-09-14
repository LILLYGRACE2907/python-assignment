# Question 14
# Create a function that accepts a number and calculates its factorial.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial =", factorial(5))
