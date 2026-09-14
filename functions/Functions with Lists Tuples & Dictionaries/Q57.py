# Question 57
# Create a function that accepts a list of numbers and returns a dictionary containing the count of even and odd numbers.

def even_odd_count(numbers):
    result = {"even": 0, "odd": 0}
    for n in numbers:
        if n % 2 == 0:
            result["even"] += 1
        else:
            result["odd"] += 1
    return result

print(even_odd_count([1, 2, 3, 4, 5, 6]))
