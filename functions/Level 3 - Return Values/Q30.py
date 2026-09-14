# Question 30
# Create a function that accepts a list of numbers and returns both the largest and smallest numbers.

def largest_smallest(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n
    return largest, smallest

print(largest_smallest([10, 5, 30, 2, 20]))
