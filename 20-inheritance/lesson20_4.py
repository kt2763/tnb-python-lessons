class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, damage):
        """ダメージを受ける"""
        self.hp -= damage
        print(f"{self.name}は{damage}ダメージを受けた! 残りHP:{self.hp}")


class Tank(Character):
    """タンククラス(防御力が高い)"""

    def __init__(self, name, hp, defense):
        super().__init__(name, hp)
        self.defense = defense

    def take_damage(self, damage):
        """ダメージを軽減して受ける(オーバーライド)"""
        reduced_damage = max(1, damage - self.defense)
        # 親クラスのtake_damageを呼び出す
        super().take_damage(reduced_damage)
        print(f"({self.defense}ダメージを防御した!)")


# 使用例
tank = Tank("騎士", 200, 10)
tank.take_damage(30)
# 騎士は20ダメージを受けた! 残りHP:180
# (10ダメージを防御した!)
