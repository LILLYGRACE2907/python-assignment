# Python Lists – Practice Question 35
# Question: Add five user-entered values to an empty list.

numbers = []
for i in range(5):
    value = int(input("Enter a number: "))
    numbers.append(value)
print(numbers)
