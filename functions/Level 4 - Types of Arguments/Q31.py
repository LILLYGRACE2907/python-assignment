# Question 31
# Create a function using default arguments to calculate the total price of a product with a default tax percentage.

def total_price(price, tax=5):
    return price + (price * tax / 100)

print("Total price =", total_price(1000))
