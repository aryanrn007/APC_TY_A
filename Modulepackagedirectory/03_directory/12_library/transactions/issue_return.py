from books.book_records import find_book

def issue_book(book_id):
    book = find_book(book_id)
    if book is None: return "Book not found."
    if not book["available"]: return "Book is already issued."
    book["available"] = False
    return f'Issued: {book["title"]}'

def return_book(book_id):
    book = find_book(book_id)
    if book is None: return "Book not found."
    book["available"] = True
    return f'Returned: {book["title"]}'
