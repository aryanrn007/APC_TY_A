BOOKS = [
    {"id": 1, "title": "Python Basics", "available": True},
    {"id": 2, "title": "Java Programming", "available": True},
]
def display_books():
    for book in BOOKS: print(book)
def find_book(book_id):
    return next((b for b in BOOKS if b["id"] == book_id), None)
