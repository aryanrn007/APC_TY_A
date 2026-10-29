# Program 9: Remove duplicate elements while preserving order
n = int(input("How many elements? "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

unique = []
for value in arr:
    if value not in unique:
        unique.append(value)

print("Original array:", arr)
print("Array without duplicates:", unique)
