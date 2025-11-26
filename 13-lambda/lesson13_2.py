numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)
print(list(result))  # [2, 4, 6, 8, 10]

print([x * 2 for x in numbers])


def double(x):
    return x * 2


result = map(double, numbers)
print(list(result))  # [2, 4, 6, 8, 10]
