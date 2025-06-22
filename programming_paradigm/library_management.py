# this script implements a system that tracks books in a library
# focusing on classes, object instantiation, and method invocation

class Book:
    """A class representing a book in a library system."""
    
    def __init__(self, title, author):
        """
        Initialize a Book with title and author.
        Books start as available (not checked out).
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute
    
    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as returned if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Return availability status of the book."""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize an empty library."""
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """Add a new book to the library's collection."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise ValueError("Can only add Book objects to the library")
    
    def check_out_book(self, title):
        """
        Check out a book by title if available.
        Returns True if successful, False otherwise.
        """
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                return book.check_out()
        return False
    
    def return_book(self, title):
        """
        Return a book by title if it was checked out.
        Returns True if successful, False otherwise.
        """
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                return book.return_book()
        return False
    
    def list_available_books(self):
        """Print all currently available books."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books currently available")
        else:
            for book in available_books:
                print(book)