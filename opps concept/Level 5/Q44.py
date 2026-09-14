# Question 44
# Create a Library that HAS-A books and USES-A search service.

class Book:
    def __init__(self, name):
        self.name = name

class SearchService:
    def use(self):
        print("SearchService used")

class Library:
    def __init__(self):
        self.items = [Book("Item 1"), Book("Item 2")]

    def run(self):
        print("Library has:", [x.name for x in self.items])
        SearchService().use()

obj = Library()
obj.run()
