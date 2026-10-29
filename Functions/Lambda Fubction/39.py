a = list(map(int, input("Enter numbers: ").split()))
result = list(map(lambda x: x * x, a))
print(result)