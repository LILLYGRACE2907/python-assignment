# Python Lists – Practice Question 16
# Question: Count positive, negative, and zero values.

numbers = [5, -2, 0, 7, -4, 0, 3]
positive = negative = zero = 0
for n in numbers:
    if n > 0:
        positive += 1
    elif n < 0:
        negative += 1
    else:
        zero += 1
print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
