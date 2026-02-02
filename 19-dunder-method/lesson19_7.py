class Vector2D:
    """2D座標クラス"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """+ 演算子"""
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """- 演算子"""
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """* 演算子(スカラー倍)"""
        return Vector2D(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"


# 使用例
pos1 = Vector2D(10, 20)
pos2 = Vector2D(5, 8)

# 座標を足し算
result = pos1 + pos2
print(result)  # Vector2D(15, 28)

# 座標を引き算
result = pos1 - pos2
print(result)  # Vector2D(5, 12)

# 座標を2倍
result = pos1 * 2
print(result)  # Vector2D(20, 40)
