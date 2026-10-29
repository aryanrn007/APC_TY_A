# 4. Find maximum and minimum in a tuple
values = tuple(int(x) for x in input("Enter integers separated by spaces: ").split())
if values:
    print("Maximum:", max(values))
    print("Minimum:", min(values))
else:
    print("Tuple is empty.")
