data = (
    [10, 20, 30],
    [40, 50, 60]
)

print("Before:", data)

data[0][1] = 100
data[1].append(70)

print("After:", data)