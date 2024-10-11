class Book:
    def __init__(self, title, author):
        # Public attributes
        self.title = title
        self.author = author
        # Private attribute to track availability
        self._is_checked_out = False
    
    def check_out(self):
        # Mark the book as checked out
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        # Mark the book as available
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        # Return True if the book is available
        return not self._is_checked_out


class Library:
    def __init__(self):
        # Private list to store books
        self._books = []
    
    def add_book(self, book):
        # Add a book to the library
        self._books.append(book)
    
    def check_out_book(self, title):
        # Check out a book by title
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    # print(f"The book '{title}' has been checked out.")
                    return True
        print(f"The book '{title}' is either not available or already checked out.")
        return False
    
    def return_book(self, title):
        # Return a book by title
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    # print(f"The book '{title}' has been returned.")
                    return True
        print(f"The book '{title}' is either not checked out or doesn't exist in the library.")
        return False
    
    def list_available_books(self):
        # List all available books in the library
        available_books = [(book.title, book.author) for book in self._books if book.is_available()]
        if available_books:
            for title, author in available_books:
                print(f"{title} by {author}")
        else:
            print("No books are currently available.")
