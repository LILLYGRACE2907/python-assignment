# Question 65
# Create a Shopping Cart System using Functions with add product, remove product, display cart, calculate total, and checkout.

cart = {}

def add_product():
    name = input("Product: ")
    price = float(input("Price: "))
    cart[name] = price

def remove_product():
    name = input("Product: ")
    if name in cart:
        del cart[name]

def display_cart():
    for name, price in cart.items():
        print(name, ":", price)

def calculate_total():
    return sum(cart.values())

def checkout():
    display_cart()
    print("Total =", calculate_total())
    print("Checkout complete")

while True:
    print("\n1.Add 2.Remove 3.Display 4.Total 5.Checkout 6.Exit")
    choice = input("Choice: ")
    if choice == "1": add_product()
    elif choice == "2": remove_product()
    elif choice == "3": display_cart()
    elif choice == "4": print(calculate_total())
    elif choice == "5": checkout()
    elif choice == "6": break
    else: print("Invalid choice")
