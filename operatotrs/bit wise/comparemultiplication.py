a = int(input("Enter a number: "))

multiplication = a * 2
left_shift = a << 1

print("Multiplication =", multiplication)
print("Left Shift =", left_shift)

if multiplication == left_shift:
    print("Both results are equal")
else:
    print("Both results are different")