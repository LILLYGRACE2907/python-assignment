products = {
    "Laptop": 50000,
    "Mouse": 500,
    "Mobile": 15000,
    "Keyboard": 1000,
    "Tablet": 20000
}

expensive_products = set()

for product, price in products.items():
    if price > 5000:
        expensive_products.add(product)

print("Products above ₹5,000:", expensive_products)