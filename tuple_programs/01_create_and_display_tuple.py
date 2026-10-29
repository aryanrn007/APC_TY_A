# 1. Create and display a tuple
items = input("Enter items separated by commas: ").split(",")
data = tuple(item.strip() for item in items)
print("Tuple:", data)
