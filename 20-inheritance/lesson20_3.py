class Character:
    """キャラクターの基本クラス"""

    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self):
        """通常攻撃"""
        print(f"{self.name}の攻撃! {self.attack_power}ダメージ!")
        return self.attack_power


class Warrior(Character):
    """戦士クラス"""

    def attack(self):
        """戦士の攻撃(オーバーライド)"""
        damage = self.attack_power * 1.5  # 1.5倍のダメージ
        print(f"{self.name}の強力な一撃! {damage}ダメージ!")
        return damage


# 使用例
warrior = Warrior("戦士", 150, 30)

warrior.attack()  # 戦士の強力な一撃! 45.0ダメージ!
