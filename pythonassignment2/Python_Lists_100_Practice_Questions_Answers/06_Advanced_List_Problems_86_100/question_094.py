# Python Lists – Practice Question 94
# Question: Find the longest increasing subsequence in a list.

numbers = [10, 22, 9, 33, 21, 50, 41, 60]
dp = [1] * len(numbers)
prev = [-1] * len(numbers)

for i in range(len(numbers)):
    for j in range(i):
        if numbers[j] < numbers[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prev[i] = j

idx = dp.index(max(dp))
result = []
while idx != -1:
    result.append(numbers[idx])
    idx = prev[idx]

result.reverse()
print(result)
