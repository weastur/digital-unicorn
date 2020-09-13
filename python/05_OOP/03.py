class Book:

    def __init__(self, author, name, year):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f"{self.name} ({self.author}) - {self.year}"


class Library:

    def __init__(self):
        self._library = []

    def search_by_name(self, name):
        for book in self._library:
            if book.name == name:
                return book

    def search_by_author(self, author):
        for book in self._library:
            if book.author == author:
                return book

    def search_by_year(self, year):
        for book in self._library:
            if book.year == year:
                return book

    def add(self, book):
        self._library.append(book)

    def delete(self, book):
        for current in self._library:
            if current.name == book.name and current.year == book.year and current.author == book.author:
                self._library.remove(current)
                return

    def sort_by_name(self):
        return sorted(self._library, key=lambda book: book.name)

    def sort_by_author(self):
        return sorted(self._library, key=lambda book: book.author)

    def sort_by_year(self):
        return sorted(self._library, key=lambda book: book.year)


b1 = Book("book1", "author1", 1972)
b2 = Book("book2", "author2", 1958)
b3 = Book("book3", "author2", 1990)

library = Library()
library.add(b1)
library.add(b2)
library.add(b3)
print(library.sort_by_name())
print(library.sort_by_author())
library.delete(b3)
print(library.sort_by_year())