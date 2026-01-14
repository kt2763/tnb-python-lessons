class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def heal(self, amount):
        """回復する"""
        self.hp += amount
        print(f"{amount}回復した! HP:{self.hp}")


player = Player("勇者", 50)
player.heal(30)  # 30回復した! HP:80
