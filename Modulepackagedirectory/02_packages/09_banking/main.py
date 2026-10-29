from banking.account import create_account, get_balance
from banking.transaction import deposit, withdraw
from banking.loan import total_repayment

account = create_account(input("Account holder name: "), float(input("Opening balance: ")))
deposit(account, float(input("Deposit amount: ")))
try:
    withdraw(account, float(input("Withdrawal amount: ")))
except ValueError as error:
    print("Withdrawal error:", error)
print("Account holder:", account["name"])
print("Current balance:", get_balance(account))
p = float(input("Loan principal: "))
r = float(input("Annual interest rate (%): "))
y = float(input("Loan period (years): "))
print("Total loan repayment (simple interest):", total_repayment(p, r, y))
