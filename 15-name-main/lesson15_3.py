# enemy.py
class Enemy:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(f"{self.name}が攻撃!")


# テストコード = これがimport時に実行されると困る
# enemy = Enemy("ゴブリン")
# enemy.attack()

if __name__ == "__main__":
    # 直接実行されたときだけ実行されるコード
    enemy = Enemy("ゴブリン")
    enemy.attack()
