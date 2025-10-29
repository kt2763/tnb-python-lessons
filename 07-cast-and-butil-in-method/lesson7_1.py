# 明示的な型変換
x = "123"
num = int(x)  # 文字列 → 整数
print(num + 10)  # 133

y = 3.5
print(int(y))  # 小数 → 整数（切り捨て）
print(float(10))  # 整数 → 小数
