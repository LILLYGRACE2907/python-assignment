# Python Lists – Practice Question 7
# Question: Count how many times a given number occurs in a list.

numbers = [2, 4, 2, 6, 2, 8, 4]
target = 2
count = 0
for n in numbers:
    if n == target:
        count += 1
print("Count:", count)
