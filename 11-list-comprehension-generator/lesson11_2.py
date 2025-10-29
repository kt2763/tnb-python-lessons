g = (i * 2 for i in range(5))
print(g)  # <generator object ...>
print(next(g))  # 0
print(next(g))  # 2
