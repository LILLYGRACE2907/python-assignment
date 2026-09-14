price = float(input("Enter shopping amount: "))
discount = 0

if price >= 5000:
    discount = 20
elif price >= 2000:
    discount = 10
else:
    discount = 5

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount =", discount, "%")
print("Discount Amount =", discount_amount)
print("Final Price =", final_price)