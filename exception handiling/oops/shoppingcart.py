class InvalidProductError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


class ShoppingCart:
    def __init__(self):
        self.products = {
            "Book": 200,
            "Pen": 50,
            "Bag": 500
        }

    def add_product(self, name, quantity):
        try:
            if name not in self.products:
                raise InvalidProductError("Product not found")

            if quantity <= 0:
                raise InvalidQuantityError(
                    "Quantity must be greater than zero"
                )

            total = self.products[name] * quantity

            print("Product:", name)
            print("Total:", total)

        except InvalidProductError as e:
            print(e)

        except InvalidQuantityError as e:
            print(e)


cart = ShoppingCart()

cart.add_product("Book", 2)
cart.add_product("Laptop", 1)
cart.add_product("Pen", 0)