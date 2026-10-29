# Program 3: Find the largest element
n = int(input("How many elements? "))
if n <= 0:
    print("Please enter at least one element.")
else:
    arr = []
    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    print("Array:", arr)
    print("Largest element:", max(arr))
