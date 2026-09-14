# Question 60
# Create a function that accepts a list of numbers and returns a dictionary containing each number and its square.

def square_dictionary(numbers):
    result = {}
    for n in numbers:
        result[n] = n * n
    return result

print(square_dictionary([1, 2, 3, 4, 5]))
