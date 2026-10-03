# Python Lists – Practice Question 67
# Question: Create a list containing "Even" or "Odd" for each number.

numbers = [1, 2, 3, 4, 5]
result = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(result)
