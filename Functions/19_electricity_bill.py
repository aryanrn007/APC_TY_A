def electricity_bill(units):
    # Example slabs: first 100 units at Rs. 3, next 100 at Rs. 5,
    # and units above 200 at Rs. 7.
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 100 * 3 + (units - 100) * 5
    else:
        bill = 100 * 3 + 100 * 5 + (units - 200) * 7
    return bill

units = float(input("Enter units consumed: "))
print("Electricity bill = Rs.", electricity_bill(units))
