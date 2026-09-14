# Question 25
# Create a function that accepts a list and returns a new list containing only odd numbers.

def odd_numbers(numbers):
    result = []
    for n in numbers:
        if n % 2 != 0:
            result.append(n)
    return result

print(odd_numbers([1, 2, 3, 4, 5, 6]))
