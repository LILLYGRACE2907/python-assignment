# Python Lists – Practice Question 98
# Question: Find the product of all elements except the current element without using division.

numbers = [1, 2, 3, 4]
result = [1] * len(numbers)

prefix = 1
for i in range(len(numbers)):
    result[i] = prefix
    prefix *= numbers[i]

suffix = 1
for i in range(len(numbers) - 1, -1, -1):
    result[i] *= suffix
    suffix *= numbers[i]

print(result)
