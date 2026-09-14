class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __gt__(self, other):
        return self.price > other.price


b1 = Book("Python", 500)
b2 = Book("Java", 400)

if b1 > b2:
    print("Python book is more expensive")
else:
    print("Java book is more expensive")