class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"Book '{self.title}' by {self.author} has been borrowed.")
        else:
            print(f"Sorry, '{self.title}' is not available for borrowing.")

    def return_book(self):
        self.is_available = True
        print(f"Book '{self.title}' by {self.author} has been returned.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} has been added to the library.")

    def display_books(self):
        print("List of books:")
        for book in self.books:
            availability = "Available" if book.is_available else "Not Available"
            print(f"'{book.title}' by {book.author} - {availability}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return
        print(f"Sorry, '{title}' is not in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"Sorry, '{title}' is not in the library.")


def main():
    library = Library()

    while True:
        print("==============Welcome to Library Management System==============")
        print("Select an option:")
        print("1. Add a book")
        print("2. Display available books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            library.add_book(title, author)
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            title = input("Enter the title of the book to borrow: ")
            library.borrow_book(title)
        elif choice == "4":
            title = input("Enter the title of the book to return: ")
            library.return_book(title)
        elif choice == "5":
            print("Goodbye! Thank you for using the Library Management System.")
            break
        else:
            print("Invalid option. Please select a valid option.")


if __name__ == "__main__":
    main()
