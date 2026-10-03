# Python Lists – Practice Question 93
# Question: Find the longest consecutive sequence of integers.

numbers = [100, 4, 200, 1, 3, 2]
numbers = sorted(numbers)
longest = current = 1
for i in range(1, len(numbers)):
    if numbers[i] == numbers[i - 1] + 1:
        current += 1
    elif numbers[i] != numbers[i - 1]:
        current = 1
    longest = max(longest, current)
print("Longest length:", longest)
