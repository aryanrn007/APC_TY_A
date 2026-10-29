# Program 6: Count even and odd elements
n = int(input("How many elements? "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

even_count = sum(1 for x in arr if x % 2 == 0)
odd_count = sum(1 for x in arr if x % 2 != 0)

print("Array:", arr)
print("Even elements:", even_count)
print("Odd elements:", odd_count)
