products = {
    "Laptop": 5,
    "Mouse": 20,
    "Keyboard": 7,
    "Monitor": 15,
    "Pen": 3
}

for product, quantity in products.items():
    if quantity < 10:
        print(product, ":", quantity)