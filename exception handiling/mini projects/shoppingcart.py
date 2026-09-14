class InvalidProductError(Exception):
    pass


class InsufficientStockError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


products = [
    Product("Book", 200, 10),
    Product("Pen", 50, 5),
    Product("Bag", 500, 3)
]


def buy_product(name, quantity):

    if quantity <= 0:
        raise InvalidQuantityError("Quantity must be greater than zero")

    for product in products:

        if product.name == name:

            if quantity > product.stock:
                raise InsufficientStockError("Insufficient stock")

            total = product.price * quantity
            product.stock -= quantity

            print("Product:", name)
            print("Total:", total)
            return

    raise InvalidProductError("Product not found")


try:
    buy_product("Book", 2)

except InvalidProductError as e:
    print(e)

except InsufficientStockError as e:
    print(e)

except InvalidQuantityError as e:
    print(e)