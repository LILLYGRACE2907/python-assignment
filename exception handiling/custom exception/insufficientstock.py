class InsufficientStockError(Exception):
    pass


try:
    stock = 10
    quantity = int(input("Enter quantity: "))

    if quantity > stock:
        raise InsufficientStockError("Not enough stock")

    stock = stock - quantity

    print("Product sold")
    print("Remaining stock:", stock)

except InsufficientStockError as e:
    print(e)