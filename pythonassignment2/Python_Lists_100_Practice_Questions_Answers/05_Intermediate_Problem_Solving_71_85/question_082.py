# Python Lists – Practice Question 82
# Question: Find the element that occurs most frequently.

numbers = [1, 2, 2, 3, 2, 4, 3]
most = numbers[0]
max_count = 0
for n in numbers:
    count = numbers.count(n)
    if count > max_count:
        max_count = count
        most = n
print("Most frequent:", most)
