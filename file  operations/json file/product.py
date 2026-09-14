import json

products = [
    {"name": "Laptop", "price": 50000, "quantity": 2},
    {"name": "Mouse", "price": 500, "quantity": 5},
    {"name": "Keyboard", "price": 1000, "quantity": 3}
]

file = open("products.json", "w")

json.dump(products, file, indent=4)

file.close()