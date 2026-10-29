def is_prime(n):
    if n < 2: return False
    return all(n % i for i in range(2, int(n ** 0.5) + 1))

def is_armstrong(n):
    s = str(n)
    return n >= 0 and n == sum(int(d) ** len(s) for d in s)

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
