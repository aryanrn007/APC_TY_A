# Program 7: Reverse an array
n = int(input("How many elements? "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

print("Original array:", arr)
print("Reversed array:", arr[::-1])
