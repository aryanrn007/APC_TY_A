def deposit(account, amount):
    if amount <= 0: raise ValueError("Deposit must be positive.")
    account["balance"] += amount
    return account["balance"]

def withdraw(account, amount):
    if amount <= 0: raise ValueError("Withdrawal must be positive.")
    if amount > account["balance"]: raise ValueError("Insufficient balance.")
    account["balance"] -= amount
    return account["balance"]
