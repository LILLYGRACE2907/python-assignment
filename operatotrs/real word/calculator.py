a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\n--- MENU ---")
print("1. Arithmetic")
print("2. Assignment")
print("3. Comparison")
print("4. Logical")
print("5. Membership")
print("6. Identity")
print("7. Bitwise")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)
    print("Division =", a / b)

elif choice == 2:
    x = a
    x += b
    print("After += :", x)

elif choice == 3:
    print("a == b :", a == b)
    print("a > b  :", a > b)
    print("a < b  :", a < b)

elif choice == 4:
    print("a > 0 and b > 0 :", a > 0 and b > 0)
    print("a > 0 or b > 0  :", a > 0 or b > 0)
    print("not(a > 0)      :", not(a > 0))

elif choice == 5:
    numbers = [10, 20, 30, 40, 50]

    print("List =", numbers)
    print("a in list :", a in numbers)
    print("b in list :", b in numbers)

elif choice == 6:
    x = a
    y = x

    print("x is y :", x is y)

elif choice == 7:
    print("AND =", a & b)
    print("OR =", a | b)
    print("XOR =", a ^ b)
    print("NOT a =", ~a)
    print("Left Shift =", a << 1)
    print("Right Shift =", a >> 1)

else:
    print("Invalid choice")