price = float(input("Enter product price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Final Price =", final_price)