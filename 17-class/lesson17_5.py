class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


potion = Item("回復薬", 50)
print(potion.name)  # 回復薬
print(potion.price)  # 50
potion.price = 30  # 値段を変更
print(potion.price)  # 30

# potion.effect = "HP回復"  # 後から属性を追加できるが...
# print(potion.effect)  # HP回復

# 推奨: __init__で最初からすべての属性を定義する
