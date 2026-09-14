def product_price(price, quantity):
    try:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        return price * quantity

    except ValueError as e:
        return e


price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

print("Total Price:", product_price(price, quantity))