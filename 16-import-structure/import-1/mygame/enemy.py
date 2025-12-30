class Enemy:
    """敵クラス"""

    def __init__(self, name):
        self.name = name
        self.hp = 50

    def attack(self):
        print(f"{self.name}の攻撃!")
