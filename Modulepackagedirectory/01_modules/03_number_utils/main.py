import number_utils as nu

n = int(input("Enter a non-negative integer: "))
print("Prime:", nu.is_prime(n))
print("Palindrome:", nu.is_palindrome(n))
print("Armstrong:", nu.is_armstrong(n))
print("Perfect:", nu.is_perfect(n))
