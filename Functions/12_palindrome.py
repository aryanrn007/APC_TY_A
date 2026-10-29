def is_palindrome(value):
    value = str(value).lower()
    return value == value[::-1]

value = input("Enter a string or number: ")
print(is_palindrome(value))
