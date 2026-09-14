# Question 20
# Create a function that accepts a list of numbers and returns the largest number without using max().

def largest(numbers):
    largest_value = numbers[0]
    for n in numbers:
        if n > largest_value:
            largest_value = n
    return largest_value

print("Largest =", largest([10, 45, 20, 5]))
