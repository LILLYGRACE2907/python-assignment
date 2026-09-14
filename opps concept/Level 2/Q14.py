# Question 14
# Create a Library class that HAS-A multiple Book objects.

class Book:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, obj):
        self.books.append(obj)

    def show_books(self):
        print("Library contains:", [x.name for x in self.books])

obj = Library()
obj.add_book(Book("Example 1"))
obj.add_book(Book("Example 2"))
obj.show_books()
