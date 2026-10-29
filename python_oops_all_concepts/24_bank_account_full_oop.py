# OOP Concept 24: Mini project combining class, object, encapsulation and methods
class BankAccount:
    def __init__(self, holder, balance=0.0):
        self.holder = holder
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
        else:
            self.__balance += amount
            print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Withdrawal successful.")

    def show_balance(self):
        print("Account holder:", self.holder)
        print("Balance:", self.__balance)

holder = input("Enter account holder name: ")
balance = float(input("Enter opening balance: "))
account = BankAccount(holder, balance)

while True:
    print("\n1. Deposit  2. Withdraw  3. Show balance  4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        account.deposit(float(input("Deposit amount: ")))
    elif choice == "2":
        account.withdraw(float(input("Withdrawal amount: ")))
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        print("Thank you.")
        break
    else:
        print("Invalid choice.")
