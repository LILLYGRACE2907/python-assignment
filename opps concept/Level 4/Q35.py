# Question 35
# A Library has Books. Identify the relationship and implement it.

# Relationship: HAS-A

class Book:
    def show(self):
        print("Book object")

class Library:
    def __init__(self):
        self.item = Book()

    def show(self):
        print("Library has a Book")
        self.item.show()

obj = Library()
obj.show()
