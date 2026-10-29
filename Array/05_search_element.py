# Program 5: Search for an element
n = int(input("How many elements? "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

target = int(input("Enter the element to search for: "))

if target in arr:
    print(target, "found at index", arr.index(target))
else:
    print(target, "not found in the array.")
