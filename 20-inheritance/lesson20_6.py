from abc import ABC, abstractmethod


class Weapon(ABC):
    """武器の抽象クラス"""

    def __init__(self, name, power):
        self.name = name
        self.power = power

    @abstractmethod
    def attack(self):
        """子クラスで必ず実装すること"""
        pass

    @abstractmethod
    def special_attack(self):
        """子クラスで必ず実装すること"""
        pass


class Sword(Weapon):
    """剣クラス"""

    def attack(self):
        print(f"{self.name}で斬りつけた! {self.power}ダメージ!")
        return self.power

    def special_attack(self):
        damage = self.power * 2
        print(f"{self.name}の回転斬り! {damage}ダメージ!")
        return damage


# 使用例
sword = Sword("鋼の剣", 30)

sword.attack()
sword.special_attack()

# 抽象クラスは直接インスタンス化できない
# weapon = Weapon("武器", 10)  # TypeError!
