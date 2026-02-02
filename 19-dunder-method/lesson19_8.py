class Item:
    """アイテムクラス"""

    def __init__(self, name, item_id):
        self.name = name
        self.item_id = item_id

    def __eq__(self, other):
        """== 演算子"""
        if not isinstance(other, Item):
            return False
        return self.item_id == other.item_id

    def __ne__(self, other):
        """!= 演算子"""
        return not self.__eq__(other)


# 使用例
item1 = Item("薬草", 1)
item2 = Item("薬草", 1)  # 同じID
item3 = Item("薬草", 2)  # 違うID

print(item1 == item2)  # True(同じアイテム)
print(item1 == item3)  # False(違うアイテム)
print(item1 != item3)  # True
