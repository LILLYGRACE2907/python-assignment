class InsufficientStockError(Exception):
    pass


class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell(self, quantity):
        try:
            if quantity > self.stock:
                raise InsufficientStockError("Not enough stock")

            self.stock = self.stock - quantity

            print("Product sold")
            print("Remaining stock:", self.stock)

        except InsufficientStockError as e:
            print(e)


product = Product("Laptop", 10)

product.sell(4)
product.sell(8)