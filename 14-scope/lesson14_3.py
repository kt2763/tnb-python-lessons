count = 0


def inc():
    global count
    count += 1


inc()
inc()
print(count)  # 2
