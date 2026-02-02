class Inventory:
    """インベントリクラス"""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __contains__(self, item):
        """in 演算子で呼ばれる"""
        return item in self.items


# 使用例
inventory = Inventory()
inventory.add_item("薬草")
inventory.add_item("鋼の剣")
inventory.add_item("盾")

# in演算子が使える!
if "鋼の剣" in inventory:
    print("鋼の剣を持っています")

if "聖剣" in inventory:
    print("聖剣を持っています")
else:
    print("聖剣を持っていません")
