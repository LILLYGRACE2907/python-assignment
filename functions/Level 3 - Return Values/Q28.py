# Question 28
# Create a function that accepts a list and removes duplicate values.

def remove_duplicates(values):
    result = []
    for value in values:
        if value not in result:
            result.append(value)
    return result

print(remove_duplicates([1, 2, 2, 3, 1, 4]))
