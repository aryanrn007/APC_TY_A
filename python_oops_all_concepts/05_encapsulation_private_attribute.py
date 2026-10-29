# OOP Concept 5: Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # name-mangled private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def show_balance(self):
        print("Account holder:", self.owner)
        print("Balance:", self.__balance)

owner = input("Enter account holder name: ")
balance = float(input("Enter starting balance: "))
account = BankAccount(owner, balance)
deposit = float(input("Enter deposit amount: "))
account.deposit(deposit)
account.show_balance()
