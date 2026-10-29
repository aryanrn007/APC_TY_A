import calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

try:
    if op == "+": result = calculator.add(a, b)
    elif op == "-": result = calculator.subtract(a, b)
    elif op == "*": result = calculator.multiply(a, b)
    elif op == "/": result = calculator.divide(a, b)
    else: raise ValueError("Invalid operation.")
    print("Result:", result)
except ValueError as error:
    print("Error:", error)
