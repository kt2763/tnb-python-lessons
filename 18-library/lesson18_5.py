import math

# 円周率
print(f"π = {math.pi}")

# 平方根
distance = math.sqrt(100)
print(f"√100 = {distance}")

# 累乗
power = math.pow(2, 10)
print(f"2の10乗 = {power}")

# 切り上げ・切り捨て・四捨五入
print(f"切り上げ: {math.ceil(4.2)}")  # 5
print(f"切り捨て: {math.floor(4.8)}")  # 4
print(f"四捨五入: {round(4.5)}")  # 4 (組み込み関数)

# 三角関数(ラジアン)
angle_rad = math.radians(45)  # 度→ラジアン変換
print(f"sin(45°) = {math.sin(angle_rad):.3f}")
print(f"cos(45°) = {math.cos(angle_rad):.3f}")

# 絶対値(組み込み関数)
print(f"絶対値: {abs(-10)}")  # 10
