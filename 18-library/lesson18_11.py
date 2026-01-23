from itertools import combinations, permutations, product

# 組み合わせ(順序を区別しない)
items = ["剣", "盾", "薬"]
for combo in combinations(items, 2):
    print(combo)
# ('剣', '盾')
# ('剣', '薬')
# ('盾', '薬')

# 順列(順序を区別する)
for perm in permutations(items, 2):
    print(perm)
# ('剣', '盾')
# ('剣', '薬')
# ('盾', '剣')
# ('盾', '薬')
# ('薬', '剣')
# ('薬', '盾')

# 直積(すべての組み合わせ)
weapons = ["剣", "槍"]
shields = ["木の盾", "鋼の盾"]
for equipment in product(weapons, shields):
    print(equipment)
# ('剣', '木の盾')
# ('剣', '鋼の盾')
# ('槍', '木の盾')
# ('槍', '鋼の盾')
