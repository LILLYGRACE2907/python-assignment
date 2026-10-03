# Python Lists – Practice Question 84
# Question: Find all pairs whose sum equals a given number.

numbers = [1, 2, 3, 4, 5, 6]
target = 7
pairs = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))
print(pairs)
