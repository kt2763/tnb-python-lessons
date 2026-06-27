import itertools

data = range(100)  # 0〜99

# 先頭10件だけ取り出す
first_10 = list(itertools.islice(data, 10))
print(first_10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 10番目から20番目まで
slice_10_20 = list(itertools.islice(data, 10, 20))
print(slice_10_20)  # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
