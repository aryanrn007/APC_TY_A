def create_account(name, opening_balance=0):
    if opening_balance < 0: raise ValueError("Opening balance cannot be negative.")
    return {"name": name, "balance": opening_balance}

def get_balance(account):
    return account["balance"]
