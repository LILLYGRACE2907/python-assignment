class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

    def display(self):
        print(self.brand, self.ram, "GB RAM", 
              self.storage, "GB Storage", self.price)


l1 = Laptop("HP", 8, 512, 55000)
l2 = Laptop("Dell", 16, 512, 65000)
l3 = Laptop("Lenovo", 8, 256, 45000)

l1.display()
l2.display()
l3.display()