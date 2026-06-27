import itertools

players = ["A", "B", "C", "D"]

# 2人の組み合わせ（順序なし）
pairs = list(itertools.combinations(players, 2))
print(pairs)
# [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]

# 2人の順列（順序あり）
ordered = list(itertools.permutations(players, 2))
print(len(ordered))  # 12通り
