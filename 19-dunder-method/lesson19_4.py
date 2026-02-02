class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def __repr__(self):
        """デバッグ用の詳細表示"""
        return f"Enemy(name='{self.name}', hp={self.hp}, attack={self.attack})"

    def __str__(self):
        """ユーザー向けの表示"""
        return f"{self.name}(HP:{self.hp})"


enemy = Enemy("ドラゴン", 500, 80)
print(enemy)  # ドラゴン(HP:500)
print(repr(enemy))  # Enemy(name='ドラゴン', hp=500, attack=80)
