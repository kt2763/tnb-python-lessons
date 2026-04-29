from abc import ABC, abstractmethod


class Shape(ABC):
    """図形の抽象基底クラス"""

    @abstractmethod
    def area(self) -> float:
        """面積を返す"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """周の長さを返す"""
        pass

    def describe(self) -> str:
        """概要を表示する（具体的な実装あり）"""
        return f"面積: {self.area():.2f}, 周の長さ: {self.perimeter():.2f}"


class Rectangle(Shape):
    """長方形"""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    """円"""

    import math

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        import math

        return math.pi * self.radius**2

    def perimeter(self) -> float:
        import math

        return 2 * math.pi * self.radius


rect = Rectangle(4, 3)
circle = Circle(5)

print(rect.describe())  # 面積: 12.00, 周の長さ: 14.00
print(circle.describe())  # 面積: 78.54, 周の長さ: 31.42
