data = [1, 2, 3]
a, b, c = data
print(a, b, c)  # 1 2 3

colors = ("red", "green", "blue")
x, y, z = colors
print(x, y, z)  # red green blue

nums = [10, 20, 30, 40, 50]
a, *b, c = nums
print(a)  # 10
print(b)  # [20, 30, 40]
print(c)  # 50
