# 8. Sort tuple values
values = tuple(int(x) for x in input("Enter integers separated by spaces: ").split())
print("Original tuple:", values)
print("Sorted tuple:", tuple(sorted(values)))
