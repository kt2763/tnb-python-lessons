class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        """print()やstr()で呼ばれる"""
        return f"{self.name}({self.price}ゴールド)"


item = Item("回復薬", 50)
print(item)  # 回復薬(50ゴールド)
print(str(item))  # 回復薬(50ゴールド)
