class Enemy:
    def __init__(self, name):
        self.name = name  # このインスタンスのname属性

    def introduce(self):
        print(f"私は{self.name}だ!")  # self.nameで自分の名前にアクセス


# 使用例
slime = Enemy("スライム")
slime.introduce()  # 私はスライムだ!

goblin = Enemy("ゴブリン")
goblin.introduce()  # 私はゴブリンだ!
