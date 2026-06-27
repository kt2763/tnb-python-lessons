import itertools

sizes = ["S", "M", "L"]
colors = ["赤", "青"]

# すべての(サイズ, 色)の組み合わせ
for size, color in itertools.product(sizes, colors):
    print(f"{size} - {color}")
# S - 赤
# S - 青
# M - 赤
# M - 青
# L - 赤
# L - 青

# 同じリストの重複あり組み合わせ（repeat引数）
dice_rolls = list(itertools.product(range(1, 7), repeat=2))
print(len(dice_rolls))  # 36通り（サイコロ2個の全パターン）
