# 5. Search for an element in a tuple
values = tuple(input("Enter items separated by spaces: ").split())
target = input("Enter item to search for: ")
if target in values:
    print("Found at index:", values.index(target))
else:
    print("Item not found.")
