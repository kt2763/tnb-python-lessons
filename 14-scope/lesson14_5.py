def counter():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count

    return inc


c = counter()
print(c())  # 1
print(c())  # 2
