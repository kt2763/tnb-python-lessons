import itertools

# cycleで無限に繰り返す
colors = itertools.cycle(["赤", "青", "緑"])
for i, color in zip(range(7), colors):
    print(f"アイテム{i}: {color}")
# アイテム0: 赤, アイテム1: 青, アイテム2: 緑, アイテム3: 赤, ...

# repeatで同じ値を繰り返す
fives = list(itertools.repeat(5, 4))
print(fives)  # [5, 5, 5, 5]
