class Book:
    # base class for all books
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    
    def __str__(self):
        """String representation for base Book class"""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """EBook subclass with digital-specific attributes"""
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    """String representation for EBook"""
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    # this class relies on the classes above for its attributes
    def __init__(self):
        self.books = [] # 

    # Add a book to the library collection
    def add_book(self, book):
        if self.books.append(book):
            return True
        return False
    
    # print details of all books in the library one at a time
    def list_books(self):
        for book in self.books:
            print(book)