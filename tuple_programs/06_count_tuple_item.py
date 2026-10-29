# 6. Count occurrences of an item
values = tuple(input("Enter items separated by spaces: ").split())
target = input("Enter item to count: ")
print("Tuple:", values)
print("Occurrences:", values.count(target))
