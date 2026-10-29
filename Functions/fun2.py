def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

n = int(input("Enter number: "))
print(check_even_odd(n))