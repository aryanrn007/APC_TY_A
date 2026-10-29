p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in years: "))
simple_interest = lambda p, r, t: (p * r * t) / 100
print(simple_interest(p, r, t))