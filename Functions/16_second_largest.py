def second_largest(numbers):
    unique = []
    for n in numbers:
        if n not in unique:
            unique.append(n)
    unique.sort()
    if len(unique) < 2:
        return None
    return unique[-2]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
answer = second_largest(numbers)
if answer is None:
    print("Need at least two different numbers.")
else:
    print("Second largest =", answer)
