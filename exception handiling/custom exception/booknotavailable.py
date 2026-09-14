class BookNotAvailableError(Exception):
    pass


try:
    book_available = False

    if book_available == False:
        raise BookNotAvailableError("Book is not available")

    print("Book issued")

except BookNotAvailableError as e:
    print(e)