# Question 24
# Create a function that accepts a list and returns a new list containing only even numbers.

def even_numbers(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result

print(even_numbers([1, 2, 3, 4, 5, 6]))
