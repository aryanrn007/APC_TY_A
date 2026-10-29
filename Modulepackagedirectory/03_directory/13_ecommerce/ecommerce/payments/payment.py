def make_payment(amount, method="cash"):
    if amount <= 0: return {"status": "failed", "reason": "Amount must be positive"}
    return {"status": "successful", "amount": amount, "method": method}
