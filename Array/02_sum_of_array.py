# Program 2: Find the sum of array elements
n = int(input("How many elements? "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

total = sum(arr)
print("Array:", arr)
print("Sum:", total)
