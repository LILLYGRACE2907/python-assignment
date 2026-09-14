# Question 69
# Create a Library Management System using Functions with options to add books, search books, issue books, return books, and display available books.

books = {}

def add_book():
    book = input("Book name: ")
    books[book] = "Available"

def search_book():
    book = input("Book name: ")
    print(books.get(book, "Book not found"))

def issue_book():
    book = input("Book name: ")
    if book in books and books[book] == "Available":
        books[book] = "Issued"
        print("Book issued")
    else:
        print("Book unavailable")

def return_book():
    book = input("Book name: ")
    if book in books:
        books[book] = "Available"

def display_available():
    for book, status in books.items():
        if status == "Available":
            print(book)

while True:
    print("\n1.Add 2.Search 3.Issue 4.Return 5.Available 6.Exit")
    choice = input("Choice: ")
    if choice == "1": add_book()
    elif choice == "2": search_book()
    elif choice == "3": issue_book()
    elif choice == "4": return_book()
    elif choice == "5": display_available()
    elif choice == "6": break
    else: print("Invalid choice")
