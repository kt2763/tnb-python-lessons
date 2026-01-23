from collections import defaultdict

# 通常の辞書だとKeyErrorが発生
normal_dict = {}
# normal_dict["key"] += 1  # KeyError!

# defaultdictならデフォルト値が自動設定される
counts = defaultdict(int)  # intのデフォルト値は0
counts["apple"] += 1
counts["banana"] += 1
counts["apple"] += 1
print(dict(counts))  # {'apple': 2, 'banana': 1}

# リストをデフォルト値にする
grouped = defaultdict(list)
grouped["fruits"].append("apple")
grouped["fruits"].append("banana")
grouped["vegetables"].append("carrot")
print(dict(grouped))  # {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']}
