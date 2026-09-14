# Question 6
# Create a function called divide() that accepts two numbers and returns their division result.

def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"

print("Division =", divide(10, 5))
