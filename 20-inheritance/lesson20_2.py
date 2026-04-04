class Enemy:
    def __init__(self, name, hp):
        print(f"Enemyの__init__が呼ばれた: {name}")
        self.name = name
        self.hp = hp


class Boss(Enemy):
    def __init__(self, name, hp, special_skill):
        print(f"Bossの__init__が呼ばれた: {name}")
        super().__init__(name, hp)  # 親クラスの__init__を呼び出す
        self.special_skill = special_skill


# 使用例
boss = Boss("魔王", 9999, "メテオ")
# Bossの__init__が呼ばれた: 魔王
# Enemyの__init__が呼ばれた: 魔王
