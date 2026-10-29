# APL Practical Programs: Classes and Objects

# 30. Bank account
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display(self):
        print(self.name, self.balance)

a = BankAccount("Amit")
b = BankAccount("Rahul")
a.deposit(1000)
a.withdraw(200)
a.display()
b.display()

# Library Book class (from the document)
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self):
        self.available = False

    def return_book(self):
        self.available = True

    def show(self):
        print(self.title, self.author, self.year, self.available)

book = Book("Python Basics", "A. Author", 2024)
book.show()
book.borrow()
book.show()
book.return_book()
book.show()
