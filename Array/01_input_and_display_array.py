# Program 1: Read and display array elements
n = int(input("How many elements? "))
arr = []

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

print("Array elements:", arr)
