class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):  # 第1引数はself
        print(f"{self.name}の攻撃!")
