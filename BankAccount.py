class BankAccount:
    count = 1000

    def __init__(self, name):
        self.account_holder = name
        self.balance = 0
        BankAccount.count += 1
        self.account_number = BankAccount.count

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
        else:
            print("Insufficient balance")


name1 = input("Enter first account holder name: ")
name2 = input("Enter second account holder name: ")

a1 = BankAccount(name1)
a2 = BankAccount(name2)

amount = int(input("Enter deposit amount for first account: "))
a1.deposit(amount)

amount = int(input("Enter deposit amount for second account: "))
a2.deposit(amount)

amount = int(input("Enter withdrawal amount from first account: "))
a1.withdraw(amount)

amount = int(input("Enter transfer amount from first account to second account: "))
a1.transfer(amount, a2)

print("\nFirst Account")
a1.display_balance()

print("\nSecond Account")
a2.display_balance()