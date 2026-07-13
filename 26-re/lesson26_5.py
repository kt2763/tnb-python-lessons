import re

text = "注文番号: ORD-1234 と ORD-5678 が届きました"
pattern = r"ORD-\d+"

m = re.search(pattern, text)
if m:
    print(m.group())  # ORD-1234
    print(m.start())  # 6（開始位置）
    print(m.end())  # 14（終了位置）

# matchは先頭からのマッチのみ
print(re.match(r"\d+", "123abc"))  # マッチ
print(re.match(r"\d+", "abc123"))  # None（先頭が数字でない）

# 先頭から全体がパターンに一致するか確認するには fullmatch を使う
print(re.fullmatch(r"\d+", "12345"))  # マッチ
print(re.fullmatch(r"\d+", "123ab"))  # None

result = re.findall(pattern, text)
print(result)  # ['ORD-1234', 'ORD-5678']

# 注文番号をマスクする
masked = re.sub(pattern, "ORD-****", text)
print(masked)  # 注文番号: ORD-**** と ORD-**** が届きました


# 関数を使った動的な置換
def upper_match(m):
    return m.group().upper()


re.sub(r"ord-\d+", upper_match, text, flags=re.IGNORECASE)

# カンマ、スペース、区切り文字が混在しているケース
data = "Alice, Bob;Charlie  Dave"
parts = re.split(r"[,;\s]+", data)
print(parts)  # ['Alice', 'Bob', 'Charlie', 'Dave']
