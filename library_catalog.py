class Book:
    def __init__(self, title, author, year):
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer.")

        self.title = title
        self.author = author
        self.year = year
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return True
        return False

    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            return True
        return False

    def __repr__(self):
        status = "Checked Out" if self.checked_out else "Available"
        return f'Book("{self.title}", by {self.author}, {status})'


class EBook(Book):
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)

        if file_size_mb <= 0:
            raise ValueError("File size must be greater than 0.")

        self.file_size_mb = file_size_mb

        # EBooks use a counter because multiple people
        # can check them out at the same time.
        self.checked_out = 0

    def check_out(self):
        self.checked_out += 1
        return True

    def return_book(self):
        if self.checked_out > 0:
            self.checked_out -= 1
            return True
        return False

    def __repr__(self):
        return (
            f'EBook("{self.title}", by {self.author}, '
            f'{self.file_size_mb} MB, '
            f'{self.checked_out} active checkout(s))'
        )


class Catalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book or EBook objects can be added.")

        self.books.append(book)

    def search_by_author(self, author):
        return [
            book
            for book in self.books
            if author.lower() in book.author.lower()
        ]

    def search_by_title(self, keyword):
        return [
            book
            for book in self.books
            if keyword.lower() in book.title.lower()
        ]

    def get_available(self):
        available = []

        for book in self.books:
            # EBooks are always available because multiple
            # people can check them out at the same time.
            if isinstance(book, EBook):
                available.append(book)
            elif not book.checked_out:
                available.append(book)

        return available

    def summary(self):
        total = len(self.books)
        available = len(self.get_available())
        ebooks = sum(isinstance(book, EBook) for book in self.books)

        print("Catalog Summary")
        print(f"Total books: {total}")
        print(f"Available books: {available}")
        print(f"EBooks: {ebooks}")
        print(f"Physical books: {total - ebooks}")


# -----------------------
# Test the program
# -----------------------

catalog = Catalog()

catalog.add_book(
    Book("Python Crash Course", "Eric Matthes", 2019)
)

catalog.add_book(
    Book("Clean Code", "Robert Martin", 2008)
)

catalog.add_book(
    EBook("AI Engineering", "Chip Huyen", 2025, 15.2)
)


# Search by title
results = catalog.search_by_title("python")
print(results)


# Search by author
author_results = catalog.search_by_author("martin")
print(author_results)


# Check out the first physical book
catalog.books[0].check_out()

available = catalog.get_available()
print(f"Available: {len(available)} books")


# EBook can be checked out multiple times
catalog.books[2].check_out()
catalog.books[2].check_out()

print(catalog.books[2])


# Show summary
catalog.summary()