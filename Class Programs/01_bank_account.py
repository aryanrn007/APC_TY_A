# Program 1: Bank Account using Class and Objects

class BankAccount:
    next_number = 1001

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        self.account_number = BankAccount.next_number
        BankAccount.next_number += 1

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(self.account_holder, "| Account:", self.account_number,
              "| Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer successful")
        else:
            print("Insufficient balance for transfer")


a = BankAccount("Amit")
b = BankAccount("Riya")

a.deposit(1000)
a.withdraw(200)
a.transfer(300, b)

a.display_balance()
b.display_balance()
