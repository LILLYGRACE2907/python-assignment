
class BookNotAvailableError(Exception):
    pass


class InvalidBookIDError(Exception):
    pass


class DuplicateBookError(Exception):
    pass


class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True


books = []


def add_book(book_id, title):
    for book in books:
        if book.book_id == book_id:
            raise DuplicateBookError("Book ID already exists")

    books.append(Book(book_id, title))
    print("Book added")


def issue_book(book_id):
    for book in books:
        if book.book_id == book_id:

            if not book.available:
                raise BookNotAvailableError("Book is already issued")

            book.available = False
            print("Book issued")
            return

    raise InvalidBookIDError("Invalid book ID")


try:
    add_book(101, "Python")
    add_book(102, "Java")

    issue_book(101)
    issue_book(101)

except DuplicateBookError as e:
    print(e)

except InvalidBookIDError as e:
    print(e)

except BookNotAvailableError as e:
    print(e)