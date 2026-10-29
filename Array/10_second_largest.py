# Program 10: Find the second-largest distinct element
n = int(input("How many elements? "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

distinct = sorted(set(arr), reverse=True)

if len(distinct) < 2:
    print("There is no second-largest distinct element.")
else:
    print("Array:", arr)
    print("Second-largest element:", distinct[1])
