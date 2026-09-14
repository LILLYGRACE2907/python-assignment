products = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 3),
    ("Keyboard", 1000, 2)
]

for name, price, quantity in products:
    total = price * quantity
    print(name, "Total:", total)