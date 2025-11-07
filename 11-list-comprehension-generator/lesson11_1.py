# 従来の書き方
nums = []
for i in range(5):
    nums.append(i * 2)

# リスト内包表記
nums = [i * 2 for i in range(5)]
print(nums)  # [0, 2, 4, 6, 8]

evens = [i for i in range(10) if i % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
