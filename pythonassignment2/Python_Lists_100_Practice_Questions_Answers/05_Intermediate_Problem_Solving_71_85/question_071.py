# Python Lists – Practice Question 71
# Question: Remove duplicate elements from a list without using set().

numbers = [1, 2, 2, 3, 1, 4, 3]
result = []
for n in numbers:
    if n not in result:
        result.append(n)
print(result)
