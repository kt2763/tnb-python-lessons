# 文字数を取得するラムダ関数
words = ["apple", "banana", "cherry"]
lengths = list(map(lambda s: len(s), words))
print(lengths)  # [5, 6, 6]

# 文字列を整数に変換するラムダ関数
nums = ["1", "2", "3"]
ints = list(map(int, nums))

# 0でない値をフィルタリングするラムダ関数
values = [10, 0, 5, 0, 20]
non_zero = list(filter(lambda x: x != 0, values))

# 文字列の先頭を大文字にするラムダ関数
names = ["alice", "bob", "charlie"]
cap = list(map(lambda x: x.capitalize(), names))
