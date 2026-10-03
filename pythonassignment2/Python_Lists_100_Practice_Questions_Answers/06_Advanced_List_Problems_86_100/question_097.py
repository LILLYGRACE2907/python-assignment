# Python Lists – Practice Question 97
# Question: Find the subarray with the largest sum.

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
best_sum = current_sum = numbers[0]
best_start = best_end = start = 0

for i in range(1, len(numbers)):
    if numbers[i] > current_sum + numbers[i]:
        current_sum = numbers[i]
        start = i
    else:
        current_sum += numbers[i]

    if current_sum > best_sum:
        best_sum = current_sum
        best_start = start
        best_end = i

print("Subarray:", numbers[best_start:best_end + 1])
print("Sum:", best_sum)
