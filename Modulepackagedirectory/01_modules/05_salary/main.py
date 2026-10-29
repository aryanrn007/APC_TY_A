import salary_utils as su

basic = float(input("Enter basic salary: "))
hra = float(input("Enter HRA: "))
allowance = float(input("Enter other allowance: "))
rate = float(input("Enter deduction percentage: "))

gross = su.gross_salary(basic, hra, allowance)
deduction = su.deductions(gross, rate)
print(f"Gross salary: {gross:.2f}")
print(f"Deductions: {deduction:.2f}")
print(f"Net salary: {gross - deduction:.2f}")
