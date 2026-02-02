class Player:
    def __init__(self, name, hp):
        """インスタンス作成時に呼ばれる"""
        self.name = name
        self.hp = hp
        print(f"{name}が作成されました!")


player = Player("勇者", 100)
# 勇者が作成されました!
