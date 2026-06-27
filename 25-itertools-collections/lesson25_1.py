import itertools

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

for item in itertools.chain(list1, list2, list3):
    print(item, end=" ")  # 1 2 3 4 5 6 7 8 9

# リストを結合する場合の比較
combined = list(itertools.chain(list1, list2, list3))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
