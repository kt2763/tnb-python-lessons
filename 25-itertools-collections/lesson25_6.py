import itertools

# 事前にソートが必要
data = sorted(
    [
        {"category": "A", "value": 1},
        {"category": "B", "value": 2},
        {"category": "A", "value": 3},
        {"category": "B", "value": 4},
    ],
    key=lambda x: x["category"],
)

for category, group in itertools.groupby(data, key=lambda x: x["category"]):
    items = list(group)
    print(f"カテゴリ {category}: {items}")
