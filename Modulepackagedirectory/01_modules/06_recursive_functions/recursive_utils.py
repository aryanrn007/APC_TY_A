def factorial(n):
    if n < 0: raise ValueError("n must be non-negative")
    return 1 if n <= 1 else n * factorial(n - 1)

def fibonacci(n):
    if n < 0: raise ValueError("n must be non-negative")
    if n <= 1: return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_digits(n):
    n = abs(n)
    return n if n < 10 else n % 10 + sum_digits(n // 10)

def to_binary(n):
    if n < 0: raise ValueError("n must be non-negative")
    if n < 2: return str(n)
    return to_binary(n // 2) + str(n % 2)
