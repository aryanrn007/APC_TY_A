# Program 10: Check whether a substring exists
text = input("Enter the main string: ")
substring = input("Enter the substring to search for: ")

if substring in text:
    print("Substring found.")
else:
    print("Substring not found.")
