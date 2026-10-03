# Python Lists – Practice Question 10
# Question: Print all elements of a list in reverse order.

numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])
