# Python Lists – Practice Question 38
# Question: Insert an element after every occurrence of a particular value.

numbers = [1, 2, 3, 2, 4]
target = 2
insert_value = 99
result = []
for n in numbers:
    result.append(n)
    if n == target:
        result.append(insert_value)
print(result)
