import string_utils as su

text = input("Enter text: ")
print("Vowels:", su.count_vowels(text))
print("Reversed:", su.reverse_string(text))
print("Palindrome:", su.is_palindrome(text))
print("Word count:", su.count_words(text))
print("Without spaces:", su.remove_spaces(text))
