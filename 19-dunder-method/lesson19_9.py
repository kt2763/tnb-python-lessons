class Player:
    """プレイヤークラス"""

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def __bool__(self):
        """生きているかどうか"""
        return self.hp > 0


# 使用例
player = Player("勇者", 50)

if player:  # __bool__が呼ばれる
    print(f"{player.name}は生きています")
else:
    print(f"{player.name}は倒れています")

# HPを0にする
player.hp = 0

if player:
    print(f"{player.name}は生きています")
else:
    print(f"{player.name}は倒れています")
