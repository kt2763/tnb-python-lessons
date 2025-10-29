data = [-3, -1, 1, 3]

# NG: 何行も書く
result = []
for x in data:
    if x > 0:
        result.append(x * x)

# OK: 一目で「正の値だけ平方」
result = [x * x for x in data if x > 0]
