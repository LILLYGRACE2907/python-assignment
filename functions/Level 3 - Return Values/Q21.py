# Question 21
# Create a function that accepts two numbers and returns their sum, difference, product, and division.

def operations(a, b):
    return a + b, a - b, a * b, a / b

s, d, p, q = operations(20, 5)
print("Sum =", s)
print("Difference =", d)
print("Product =", p)
print("Division =", q)
