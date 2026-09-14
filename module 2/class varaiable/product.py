class Product:
    category = "Electronics"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Category:", Product.category)


p1 = Product("Laptop", 50000)
p2 = Product("Mobile", 20000)
p3 = Product("Tablet", 15000)

p1.display()
p2.display()
p3.display()