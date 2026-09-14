# Question 29
# Create a function that accepts a list of numbers and returns the second-largest number.

def second_largest(numbers):
    unique = []
    for n in numbers:
        if n not in unique:
            unique.append(n)
    unique.sort()
    return unique[-2]

print("Second largest =", second_largest([10, 30, 20, 40, 30]))
