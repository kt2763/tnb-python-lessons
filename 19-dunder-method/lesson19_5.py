class Inventory:
    """インベントリクラス"""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        """len()で所持アイテム数を返す"""
        return len(self.items)


inventory = Inventory()
inventory.add_item("薬草")
inventory.add_item("鋼の剣")
inventory.add_item("盾")

print(f"所持アイテム数: {len(inventory)}")  # 3
