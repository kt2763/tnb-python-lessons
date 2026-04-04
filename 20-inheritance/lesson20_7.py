class Character:
    def __init__(self, name):
        self.name = name

    def greet(self):
        """挨拶(サブクラスでオーバーライドされる)"""
        pass


class Hero(Character):
    def greet(self):
        print(f"{self.name}: よろしく頼む!")


class Villain(Character):
    def greet(self):
        print(f"{self.name}: フハハハ!")


class Merchant(Character):
    def greet(self):
        print(f"{self.name}: いらっしゃいませ!")


# ポリモーフィズムの実例
characters = [Hero("勇者"), Villain("魔王"), Merchant("商人")]

# 同じメソッド名で異なる動作
for character in characters:
    character.greet()
# 勇者: よろしく頼む!
# 魔王: フハハハ!
# 商人: いらっしゃいませ!
