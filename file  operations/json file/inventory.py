import json

file = open("products.json", "r")

products = json.load(file)

total = 0

for product in products:
    total += product["price"] * product["quantity"]

print("Total Inventory Value:", total)

file.close()