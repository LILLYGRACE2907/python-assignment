class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("Product added")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print("Product removed")
                return

        print("Product not found")

    def view_cart(self):
        if len(self.products) == 0:
            print("Cart is empty")
        else:
            for product in self.products:
                print(product.name, product.price)

    def checkout(self):
        total = 0

        for product in self.products:
            total = total + product.price

        print("Total Bill:", total)


cart = ShoppingCart()


while True:
    print("\n1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))

        product = Product(name, price)
        cart.add_product(product)

    elif choice == 2:
        name = input("Enter Product Name: ")
        cart.remove_product(name)

    elif choice == 3:
        cart.view_cart()

    elif choice == 4:
        cart.checkout()

    elif choice == 5:
        break

    else:
        print("Invalid choice")