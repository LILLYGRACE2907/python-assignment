# Question 13
# Create a function that accepts three numbers and returns the smallest number.

def smallest(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= c:
        return b
    return c

print("Smallest =", smallest(10, 5, 15))
