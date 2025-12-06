def outer():
    x = 10

    def inner():
        nonlocal x
        x += 1

    inner()
    print(x)


outer()  # 11
