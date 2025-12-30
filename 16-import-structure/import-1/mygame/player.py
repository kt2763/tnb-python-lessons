class Player:
    """プレイヤークラス"""

    def __init__(self, name):
        self.name = name
        self.hp = 100

    def attack(self):
        print(f"{self.name}の攻撃!")
