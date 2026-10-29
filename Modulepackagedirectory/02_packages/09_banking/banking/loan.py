def simple_interest(principal, annual_rate, years):
    if principal < 0 or annual_rate < 0 or years < 0:
        raise ValueError("Loan values cannot be negative.")
    return principal * annual_rate * years / 100

def total_repayment(principal, annual_rate, years):
    return principal + simple_interest(principal, annual_rate, years)
