products = {
    "Laptop": 50000,
    "Mouse": 500,
    "Mobile": 15000,
    "Keyboard": 1000,
    "Tablet": 20000
}

for product, price in products.items():
    if price > 1000:
        print(product, ":", price)