# Question 70
# Create a Menu-Driven Python Application that uses separate functions for every operation and keeps running until the user selects Exit.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

def show_menu():
    print("\n1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")
    if choice == "5":
        print("Program ended")
        break
    if choice in ["1", "2", "3", "4"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == "1": print(add(a, b))
        elif choice == "2": print(subtract(a, b))
        elif choice == "3": print(multiply(a, b))
        elif choice == "4": print(divide(a, b))
    else:
        print("Invalid choice")
