class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # Book is available by default

    def __str__(self):
        return f"{self.title} by {self.author}"


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # List to store borrowed books

    def __str__(self):
        return self.name


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    # Add a new book
    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" added successfully.')

    # Register a new patron
    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f'Patron "{patron.name}" registered successfully.')

    # Borrow a book
    def borrow_book(self, patron, book):
        if book.available:
            book.available = False
            patron.borrowed_books.append(book)
            print(f'{patron.name} borrowed "{book.title}".')
        else:
            print(f'Sorry! "{book.title}" is not available.')

    # Return a book
    def return_book(self, patron, book):
        if book in patron.borrowed_books:
            book.available = True
            patron.borrowed_books.remove(book)
            print(f'{patron.name} returned "{book.title}".')
        else:
            print(f'{patron.name} has not borrowed "{book.title}".')

    # Display all books
    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book.title} by {book.author} - {status}")

    # Display borrowed books of a patron
    def display_patron_books(self, patron):
        print(f"\nBooks borrowed by {patron.name}:")
        if patron.borrowed_books:
            for book in patron.borrowed_books:
                print(book.title)
        else:
            print("No books borrowed.")


# Main Program
library = Library()

# Create books
book1 = Book("Python Programming", "John Smith")
book2 = Book("Data Structures", "Alice Brown")
book3 = Book("Machine Learning", "David Lee")

# Add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Register patrons
patron1 = Patron("Rahul")
patron2 = Patron("Sneha")

library.register_patron(patron1)
library.register_patron(patron2)

# Display books
library.display_books()

# Borrow books
library.borrow_book(patron1, book1)
library.borrow_book(patron2, book2)

# Display books after borrowing
library.display_books()

# Display borrowed books
library.display_patron_books(patron1)
library.display_patron_books(patron2)

# Return a book
library.return_book(patron1, book1)

# Display books after return
library.display_books()
