# 10. Demonstrate tuple slicing
values = tuple(input("Enter items separated by spaces: ").split())
print("Tuple:", values)
print("First three items:", values[:3])
print("Items from index 1 onward:", values[1:])
print("Tuple in reverse:", values[::-1])
