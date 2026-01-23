import re

# パターンマッチング
text = "プレイヤーIDは12345です"
match = re.search(r"\d+", text)  # 数字を検索
if match:
    print(f"見つかった数字: {match.group()}")  # 12345

# すべてのマッチを取得
text = "スコア: 100, 200, 300"
numbers = re.findall(r"\d+", text)
print(numbers)  # ['100', '200', '300']

# 置換
text = "敵を倒した! 敵を倒した!"
result = re.sub(r"敵", "モンスター", text)
print(result)  # モンスターを倒した! モンスターを倒した!

# 分割
text = "apple,banana;orange:grape"
fruits = re.split(r"[,;:]", text)  # 複数の区切り文字で分割
print(fruits)  # ['apple', 'banana', 'orange', 'grape']
