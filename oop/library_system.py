class Book:
    def __init__(self, title, author):
        """Initialize a Book instance with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook instance with title, author, and file size."""
        super().__init__(title, author)  # Call the base class initializer
        self.file_size = file_size  # Unique attribute for EBook

    def __str__(self):
        """Return a string representation of the eBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}kB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook instance with title, author, and page count."""
        super().__init__(title, author)  # Call the base class initializer
        self.page_count = page_count  # Unique attribute for PrintBook

    def __str__(self):
        """Return a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []  # List to store Book, EBook, and PrintBook instances

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        """Print details of each book in the library."""
        if self.books:
            for book in self.books:
                print(f"{book}")
        else:
            print("The library has no books.")
