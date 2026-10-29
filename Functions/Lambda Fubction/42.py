a = list(map(int, input("Enter numbers: ").split()))
result = list(filter(lambda x: x % 2 == 0, a))
print(result)