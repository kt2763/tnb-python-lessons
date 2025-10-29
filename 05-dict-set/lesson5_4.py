person = {"name": "たなべ", "age": 36}
print(*person)  # name age（キーだけ出る）

nums = {1, 2, 3}
a, b, c = nums
print(a, b, c)  # 順序は保証されない点に注意
