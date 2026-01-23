from typing import Dict, List, Optional, Tuple, Union


# 型ヒント付き関数
def calculate_damage(base_power: int, multiplier: float) -> int:
    """ダメージ計算"""
    return int(base_power * multiplier)


# リスト型
def get_item_names(items: List[str]) -> None:
    for item in items:
        print(item)


# 辞書型
def load_player_data(data: Dict[str, int]) -> None:
    print(f"HP: {data['hp']}")
    print(f"MP: {data['mp']}")


# Optional(Noneの可能性がある)
def find_item(item_name: str) -> Optional[str]:
    """アイテムを検索(見つからなければNone)"""
    items = ["剣", "盾", "薬"]
    if item_name in items:
        return item_name
    return None


# タプル型
def get_position() -> Tuple[int, int]:
    """座標を返す"""
    return (10, 20)


# Union(複数の型の可能性)
def process_value(value: Union[int, str]) -> str:
    """intまたはstrを受け取る"""
    return str(value)


# 使用例
damage = calculate_damage(50, 1.5)
get_item_names(["剣", "盾"])
load_player_data({"hp": 100, "mp": 50})
result = find_item("剣")
x, y = get_position()
