class Player:
    def __init__(self, name, level):
        self.name = name
        self._level = level

    @property
    def level(self):
        """レベルを取得"""
        return self._level

    @level.setter
    def level(self, value):
        """レベルを設定（1以上のみ）"""
        if value < 1:
            raise ValueError("レベルは1以上が必要です")
        self._level = value
        print(f"{self.name}のレベルが{value}になりました！")

    @property
    def max_hp(self):
        """レベルに応じて自動計算（()不要）"""
        return 100 + (self._level - 1) * 10


player = Player("勇者", 1)
print(player.level)  # 1 （() なしでアクセス）
print(player.max_hp)  # 100
player.level = 10  # 勇者 のレベルが 10 になりました！
print(player.max_hp)  # 190
