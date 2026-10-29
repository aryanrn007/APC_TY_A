a = list(map(int, input("Enter numbers:").split()))

def prime(n):
    if n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)):
        return True
    else:
        return False
        
result: list[int] = list(filter(lambda x: prime(x), a))
print(result)
