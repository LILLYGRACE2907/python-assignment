# Question 55
# Create a function that accepts a dictionary and returns all keys whose values are greater than 50.

def values_greater_than_50(data):
    result = []
    for key, value in data.items():
        if value > 50:
            result.append(key)
    return result

print(values_greater_than_50({"A": 40, "B": 75, "C": 60}))
