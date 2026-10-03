# Python Lists – Practice Question 64
# Question: Extract words having more than 5 characters.

words = ["python", "list", "computer", "code", "program"]
result = [word for word in words if len(word) > 5]
print(result)
