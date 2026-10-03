# Python Lists – Practice Question 99
# Question: Flatten a nested list such as [1, [2, 3], [4, [5, 6]]] into [1, 2, 3, 4, 5, 6].

nested = [1, [2, 3], [4, [5, 6]]]

def flatten(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten(nested))
