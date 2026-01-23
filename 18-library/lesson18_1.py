import random

# ランダムな整数を生成(1〜6のサイコロ)
dice = random.randint(1, 6)
print(f"サイコロの目: {dice}")

# ランダムな小数(0.0〜1.0)
value = random.random()
print(f"ランダム値: {value}")

# リストからランダムに選択
enemies = ["スライム", "ゴブリン", "ドラゴン"]
enemy = random.choice(enemies)
print(f"出現した敵: {enemy}")

# リストをシャッフル
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(f"シャッフル後: {cards}")

# 範囲を指定してランダムな小数
damage = random.uniform(10.0, 20.0)
print(f"ダメージ: {damage:.1f}")
