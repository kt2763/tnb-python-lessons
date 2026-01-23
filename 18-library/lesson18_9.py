from collections import Counter

# 文字の出現回数をカウント
text = "hello world"
counter = Counter(text)
print(
    counter
)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# 最も多い要素を取得
print(counter.most_common(2))  # [('l', 3), ('o', 2)]

# リストの要素をカウント
items = ["apple", "banana", "apple", "orange", "banana", "apple"]
item_count = Counter(items)
print(item_count)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})
