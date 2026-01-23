import json

# Pythonの辞書をJSONに変換
player_data = {
    "name": "勇者",
    "level": 10,
    "hp": 100,
    "items": ["薬草", "鋼の剣", "盾"],
}

# JSON文字列に変換
json_str = json.dumps(player_data, ensure_ascii=False, indent=2)
print(json_str)
