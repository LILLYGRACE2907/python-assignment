# Question 19
# Create a function that accepts a list of numbers and returns the total without using sum().

def total(numbers):
    result = 0
    for n in numbers:
        result += n
    return result

print("Total =", total([10, 20, 30, 40]))
