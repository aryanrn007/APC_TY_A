# OOP Concept 19: __str__ and __repr__
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r})"

title = input("Enter book title: ")
author = input("Enter author name: ")
book = Book(title, author)
print("User-friendly:", book)
print("Developer representation:", repr(book))
