# Question 43
# Create a recursive function to calculate factorial.

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Factorial =", factorial(5))
