a = list(map(int, input("Enter numbers: ").split()))
result = list(map(lambda x: x ** 3, a))
print(result)