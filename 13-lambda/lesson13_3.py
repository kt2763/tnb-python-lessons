numbers = [1, 2, 3, 4, 5, 6]

evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # [2, 4, 6]


print([x for x in numbers if x % 2 == 0])


def is_even(x):
    return x % 2 == 0


evens = filter(is_even, numbers)
print(list(evens))  # [2, 4, 6]
