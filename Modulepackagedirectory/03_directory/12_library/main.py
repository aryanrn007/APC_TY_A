from books.book_records import display_books
from members.member_records import display_members
from transactions.issue_return import issue_book, return_book

print("Books:")
display_books()
print("\nMembers:")
display_members()
print("\n", issue_book(1))
print("After issue:")
display_books()
print(return_book(1))
