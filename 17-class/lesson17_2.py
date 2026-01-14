class Player:
    """プレイヤークラス"""

    # コンストラクタ(初期化メソッド)
    def __init__(self, name, hp):
        self.name = name  # 属性
        self.hp = hp  # 属性

    # メソッド(関数)
    def attack(self):
        print(f"{self.name}が攻撃した!")

    def show_status(self):
        print(f"{self.name} HP:{self.hp}")


# インスタンスを作成
player = Player("勇者", 100)

# メソッドを呼び出す
player.attack()  # 勇者が攻撃した!
player.show_status()  # 勇者 HP:100

# 属性にアクセス
print(player.name)  # 勇者
print(player.hp)  # 100
