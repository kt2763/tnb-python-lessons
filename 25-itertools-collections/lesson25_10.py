from collections import namedtuple

# フィールド名をつけたタプル
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 5)

print(p.x)  # 3（名前でアクセス）
print(p[0])  # 3（インデックスでもアクセス可）
print(p)  # Point(x=3, y=5)

# イミュータブル（変更不可）
# p.x = 10  # AttributeError

# アンパック可能
x, y = p
print(x, y)  # 3 5
