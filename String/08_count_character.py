# Program 8: Count occurrences of a character
text = input("Enter a string: ")
character = input("Enter a character to count: ")

if len(character) != 1:
    print("Please enter exactly one character.")
else:
    print("Occurrences:", text.count(character))
