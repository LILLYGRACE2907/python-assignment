# Python Lists – Practice Question 96
# Question: Find all subarrays whose sum equals a given number.

numbers = [1, 2, 3, 2, 1]
target = 5
result = []
for i in range(len(numbers)):
    total = 0
    for j in range(i, len(numbers)):
        total += numbers[j]
        if total == target:
            result.append(numbers[i:j + 1])
print(result)
