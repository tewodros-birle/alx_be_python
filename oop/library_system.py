class Book:
    """Base class representing a book"""
    
    def __init__(self, title, author):
        """Initialize base book attributes"""
        self.title = title
        self.author = author
    
    def __str__(self):
        """String representation for base Book class"""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book"""
    
    def __init__(self, title, author, file_size):
        """Initialize eBook with additional file_size attribute"""
        super().__init__(title, author)
        self.file_size = file_size  # in KB
    
    def __str__(self):
        """String representation for EBook"""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a physical printed book"""
    
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with additional page_count attribute"""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """String representation for PrintBook"""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class demonstrating composition by managing a collection of books"""
    
    def __init__(self):
        """Initialize with empty book collection"""
        self.books = []
    
    def add_book(self, book):
        """Add a book to the library collection"""
        self.books.append(book)
    
    def list_books(self):
        """Print details of all books in the library"""
        for book in self.books:
            print(book)
