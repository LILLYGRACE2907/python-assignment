class Book:
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages

    def display(self):
        print(self.title, self.author, self.price, self.pages)


b1 = Book("Java Programming", "James", 500, 300)
b2 = Book("Python Basics", "Guido", 450, 250)
b3 = Book("Web Development", "John", 600, 400)

b1.display()
b2.display()
b3.display()