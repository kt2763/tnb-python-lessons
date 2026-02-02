class DamageCalculator:
    """ダメージ計算クラス"""

    def __init__(self, base_power):
        self.base_power = base_power

    def __call__(self, multiplier=1.0, critical=False):
        """インスタンスを関数のように呼び出せる"""
        damage = self.base_power * multiplier
        if critical:
            damage *= 2
        return int(damage)


# 使用例
calc = DamageCalculator(50)

# 関数のように呼び出せる!
print(calc())  # 50(通常)
print(calc(multiplier=1.5))  # 75(1.5倍)
print(calc(multiplier=1.5, critical=True))  # 150(1.5倍+クリティカル)
