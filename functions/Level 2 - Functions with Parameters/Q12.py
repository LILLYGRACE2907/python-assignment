# Question 12
# Create a function that accepts three numbers and returns the largest number.

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    return c

print("Largest =", largest(10, 25, 15))
