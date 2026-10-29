s = input("Enter a string: ")

vowels = 0
for ch in s.lower():
    if ch in "aeiou":
        vowels += 1

print("String:", s)
print("Number of vowels:", vowels)