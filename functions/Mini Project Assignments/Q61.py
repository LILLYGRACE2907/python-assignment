# Question 61
# Create a Calculator Program using Functions with options for addition, subtraction, multiplication, division, and modulus.

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Cannot divide by zero"
def modulus(a, b): return a % b if b != 0 else "Cannot divide by zero"

while True:
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.Modulus 6.Exit")
    choice = input("Enter choice: ")
    if choice == "6":
        break
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if choice == "1": print(add(a, b))
    elif choice == "2": print(subtract(a, b))
    elif choice == "3": print(multiply(a, b))
    elif choice == "4": print(divide(a, b))
    elif choice == "5": print(modulus(a, b))
    else: print("Invalid choice")
