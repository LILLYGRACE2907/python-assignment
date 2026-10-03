# Python Lists – Practice Question 85
# Question: Find all triplets whose sum equals a given number.

numbers = [1, 2, 3, 4, 5, 6]
target = 9
triplets = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == target:
                triplets.append((numbers[i], numbers[j], numbers[k]))
print(triplets)
