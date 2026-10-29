def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

n = int(input("How many Fibonacci numbers? "))
print(fibonacci(n))
