# Python Lists – Practice Question 95
# Question: Find the maximum sum subarray.

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
current = best = numbers[0]
for n in numbers[1:]:
    current = max(n, current + n)
    best = max(best, current)
print("Maximum subarray sum:", best)
