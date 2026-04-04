class Character:
    """キャラクターの基本クラス"""

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        print(f"{self.name}の攻撃!")

    def is_alive(self):
        """生きているかチェック"""
        return self.hp > 0


class Player(Character):
    """プレイヤークラス"""

    def __init__(self, name, hp, mp):
        # 親クラスの__init__を呼び出す
        super().__init__(name, hp)
        # プレイヤー独自の属性を追加
        self.mp = mp

    def magic(self):
        """プレイヤー独自のメソッド"""
        if self.mp >= 10:
            self.mp -= 10
            print(f"{self.name}は魔法を唱えた!(残りMP:{self.mp})")
        else:
            print("MPが足りない!")


# 使用例
player = Player("勇者", 100, 50)
player.attack()  # 勇者の攻撃!(親クラスのメソッド)
player.magic()  # 勇者は魔法を唱えた!(子クラスのメソッド)
print(player.is_alive())  # True(親クラスのメソッド)
