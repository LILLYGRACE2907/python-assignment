price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if total >= 5000 and quantity >= 2:
    discount = 20
elif total >= 2000:
    discount = 10
else:
    discount = 0

discount_amount = total * discount / 100
total -= discount_amount

if total > 0:
    print("Discount =", discount, "%")
    print("Final Bill =", total)
else:
    print("Invalid bill")