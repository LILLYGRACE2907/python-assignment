class Laptop:
    def __init__(self, brand, ram, storage, processor, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.processor = processor
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print("Processor:", self.processor)
        print("Price:", self.price)


l = Laptop("HP", "8 GB", "512 GB", "Intel i5", 55000)

l.display()