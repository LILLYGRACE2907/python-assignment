# Question 34
# Create a function using *args to calculate the sum of any number of values.

def total(*args):
    result = 0
    for n in args:
        result += n
    return result

print("Sum =", total(10, 20, 30, 40))
