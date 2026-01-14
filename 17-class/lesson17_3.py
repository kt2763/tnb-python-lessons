class Weapon:
    def __init__(self, name, power):
        print("武器が作られました!")
        self.name = name
        self.power = power


# インスタンス作成時に__init__が自動実行される
sword = Weapon("鋼の剣", 30)  # 武器が作られました!
