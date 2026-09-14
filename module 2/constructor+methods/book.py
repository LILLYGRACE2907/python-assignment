class Book:
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Pages:", self.pages)


b = Book("Python Basics", "Guido", 500, 300)

b.display()