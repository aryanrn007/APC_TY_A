def gross_salary(basic, hra, allowance):
    return basic + hra + allowance

def deductions(gross, deduction_rate):
    return gross * deduction_rate / 100

def net_salary(basic, hra, allowance, deduction_rate):
    gross = gross_salary(basic, hra, allowance)
    return gross - deductions(gross, deduction_rate)
