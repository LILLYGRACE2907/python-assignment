class BookNotAvailableError(Exception):
    pass


class Library:
    def __init__(self):
        self.books = ["Python", "Java", "SQL"]

    def issue_book(self, book):
        try:
            if book not in self.books:
                raise BookNotAvailableError("Book is not available")

            self.books.remove(book)
            print(book, "issued")

        except BookNotAvailableError as e:
            print(e)


library = Library()

library.issue_book("Python")
library.issue_book("C++")