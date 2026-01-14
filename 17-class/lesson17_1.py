class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack


# 何体でも簡単に作れる!
slime = Enemy("スライム", 50, 10)
goblin = Enemy("ゴブリン", 80, 15)
dragon = Enemy("ドラゴン", 500, 100)
