from itertools import count, cycle, repeat

# count: 無限カウンタ
counter = count(start=1, step=1)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3

# cycle: リストを無限に繰り返す
colors = cycle(["赤", "青", "緑"])
for i in range(5):
    print(next(colors))  # 赤, 青, 緑, 赤, 青

# repeat: 同じ値を繰り返す
for item in repeat("攻撃!", 3):
    print(item)  # 攻撃! 攻撃! 攻撃!
