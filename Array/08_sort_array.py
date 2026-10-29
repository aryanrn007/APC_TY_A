# Program 8: Sort array elements in ascending order
n = int(input("How many elements? "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

arr.sort()
print("Array in ascending order:", arr)
