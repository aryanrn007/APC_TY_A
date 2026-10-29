import recursive_utils as ru

n = int(input("Enter a non-negative integer: "))
print("Factorial:", ru.factorial(n))
print("Fibonacci number at position n:", ru.fibonacci(n))
print("Sum of digits:", ru.sum_digits(n))
print("Binary:", ru.to_binary(n))
